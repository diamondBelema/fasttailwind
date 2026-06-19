"""Generate safelist for Tailwind CSS purge configuration."""
from __future__ import annotations
import re
from .contracts.theme import ThemeScheme

# Shades to generate for "bare hue" color tokens (e.g. colors.primary = "violet",
# with no shade suffix). Components are free to combine a bare hue with any of
# these shades (e.g. f"text-{theme.colors.primary}-500"). If you reach for a
# shade outside this list in your own components, add it here too.
_BARE_HUE_SHADES = (400, 500, 600, 700)

_HAS_SHADE = re.compile(r"-\d{2,3}$")


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
        if not isinstance(val, str):
            continue

        # Bare hue (e.g. "violet", no shade) — expand across known shades.
        # A token with no shade suffix isn't a valid standalone Tailwind class
        # (e.g. "text-violet" doesn't exist), so only emit it combined with a shade.
        if not _HAS_SHADE.search(val):
            variants = [f"{val}-{shade}" for shade in _BARE_HUE_SHADES]
        else:
            variants = [val]

        for v in variants:
            classes.add(v)
            for prefix in ("bg", "text", "border", "ring", "fill", "stroke",
                           "from", "to", "via", "caret", "accent", "shadow"):
                classes.add(f"{prefix}-{v}")
            for state in ("hover", "focus", "active", "disabled", "dark"):
                for prefix in ("bg", "text", "border", "ring"):
                    classes.add(f"{state}:{prefix}-{v}")

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
