"""Master theme contract — defines the shape of a user's complete theme."""
from __future__ import annotations


class ThemeScheme:
    """Base class for complete themes. Variants live here — not hardcoded in components."""

    _required = [
        "colors", "typography",
        "space_xs", "space_sm", "space_md", "space_lg", "space_xl", "space_2xl",
        "radius_sm", "radius_md", "radius_lg", "radius_full",
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
