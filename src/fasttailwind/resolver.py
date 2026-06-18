"""Token resolver: converts theme tokens to Tailwind class strings."""
from __future__ import annotations
from typing import Any
from .contracts.theme import ThemeScheme


class TokenResolver:
    """Converts theme token names to Tailwind class strings at render time."""

    def __init__(self, theme: ThemeScheme) -> None:
        self._theme = theme

    @property
    def theme(self) -> ThemeScheme:
        return self._theme

    def resolve(self, token: str) -> str:
        """Resolve a dot-delimited token path to its string value."""
        parts = token.split(".")
        obj: Any = self._theme
        for part in parts:
            if obj is None:
                raise ValueError(f"Cannot resolve token '{token}': None at '{part}'")
            obj = getattr(obj, part, None)
        if obj is None:
            raise ValueError(f"Unknown token: '{token}'")
        if not isinstance(obj, str):
            raise ValueError(f"Token '{token}' resolved to non-string: {type(obj).__name__}")
        return obj

    def variant(self, component: str, name: str) -> str:
        """Look up a component variant class string from the theme."""
        variants = getattr(self._theme, f"{component}_variants", {})
        return variants.get(name, "") if isinstance(variants, dict) else ""

    def size(self, component: str, name: str) -> str:
        """Look up a component size class string from the theme."""
        sizes = getattr(self._theme, f"{component}_sizes", {})
        return sizes.get(name, "") if isinstance(sizes, dict) else ""

    def responsive(self, prop: str, values: dict[str, Any]) -> str:
        """Convert a breakpoint dict to prefixed Tailwind class strings."""
        classes: list[str] = []
        for bp, val in values.items():
            prefix = f"{bp}:" if bp != "base" else ""
            classes.append(f"{prefix}{prop}-{val}")
        return " ".join(classes)

    def spacing(self, token: str) -> str:
        """Resolve a spacing token to its numeric Tailwind suffix."""
        return self.resolve(token if token.startswith("space_") else f"space_{token}")

    def radius(self, token: str) -> str:
        """Resolve a radius token to its Tailwind class string."""
        return self.resolve(token if token.startswith("radius_") else f"radius_{token}")
