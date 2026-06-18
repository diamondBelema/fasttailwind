"""Generate safelist for Tailwind CSS purge configuration."""
from __future__ import annotations
from .contracts.theme import ThemeScheme


def safelist(theme: ThemeScheme) -> list[str]:
    """Return every class string your theme generates."""
    classes: set[str] = set()

    for attr_name in dir(theme):
        if attr_name.endswith(("_variants", "_sizes")):
            variants = getattr(theme, attr_name, {})
            if isinstance(variants, dict):
                for cls_string in variants.values():
                    if isinstance(cls_string, str):
                        classes.update(cls_string.split())

    colors = theme.colors
    for attr_name in dir(colors):
        if attr_name.startswith("_"):
            continue
        val = getattr(colors, attr_name)
        if isinstance(val, str):
            classes.add(val)
            for prefix in ("bg", "text", "border", "ring", "fill", "stroke",
                           "from", "to", "via", "caret", "accent", "shadow"):
                classes.add(f"{prefix}-{val}")
            for state in ("hover", "focus", "active", "disabled", "dark"):
                for prefix in ("bg", "text", "border", "ring"):
                    classes.add(f"{state}:{prefix}-{val}")

    typography = theme.typography
    for attr_name in dir(typography):
        if attr_name.startswith("_"):
            continue
        val = getattr(typography, attr_name)
        if isinstance(val, str):
            classes.add(val)

    for attr_name in dir(theme):
        if attr_name.startswith("space_"):
            val = getattr(theme, attr_name)
            if isinstance(val, str):
                for prefix in ("p", "px", "py", "m", "mx", "my", "gap", "space-x", "space-y"):
                    classes.add(f"{prefix}-{val}")

    for attr_name in dir(theme):
        if attr_name.startswith("radius_"):
            val = getattr(theme, attr_name)
            if isinstance(val, str):
                classes.add(val)

    return sorted(classes)
