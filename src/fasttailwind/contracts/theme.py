"""Master theme contract — defines the shape of a user's complete theme."""
from __future__ import annotations

# Attributes that must be a dict (of variant-name -> Tailwind class string).
_DICT_ATTRS = (
    "breakpoints",
    "button_variants", "button_sizes",
    "card_variants", "badge_variants",
    "input_variants", "alert_variants",
)

# Attributes that must be a plain string (e.g. "4", "rounded-lg").
_STR_ATTRS = (
    "space_xs", "space_sm", "space_md", "space_lg", "space_xl", "space_2xl",
    "radius_sm", "radius_md", "radius_lg", "radius_full",
)


class ThemeScheme:
    """Base class for complete themes. Variants live here — not hardcoded in components."""

    _required = [
        "colors", "typography",
        *_STR_ATTRS,
        "breakpoints",
        "button_variants", "button_sizes",
        "card_variants", "badge_variants",
        "input_variants", "alert_variants",
    ]

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        missing = [a for a in cls._required if not hasattr(cls, a)]
        if missing:
            raise NotImplementedError(
                f"{cls.__name__} missing required theme attributes: {missing}"
            )

        wrong_type: list[str] = []
        for attr in _STR_ATTRS:
            if not isinstance(getattr(cls, attr), str):
                wrong_type.append(attr)
        for attr in _DICT_ATTRS:
            val = getattr(cls, attr)
            if not isinstance(val, dict):
                wrong_type.append(attr)
            elif attr != "breakpoints" and not all(isinstance(v, str) for v in val.values()):
                # *_variants / *_sizes dicts must map name -> Tailwind class string
                wrong_type.append(f"{attr} (values must all be str)")
        if wrong_type:
            raise TypeError(
                f"{cls.__name__} has incorrectly-typed theme attributes: {wrong_type}"
            )
