"""Typography scheme contract — defines the shape of a user's typography theme."""
from __future__ import annotations


class TypographyScheme:
    """Base class for typography themes. Subclass and set all required attributes."""

    _required = [
        "font_sans", "font_mono",
        "size_xs", "size_sm", "size_base", "size_lg", "size_xl", "size_2xl", "size_3xl",
        "weight_normal", "weight_medium", "weight_bold",
        "leading_tight", "leading_normal", "leading_relaxed",
    ]

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        missing = [a for a in cls._required if not hasattr(cls, a)]
        if missing:
            raise NotImplementedError(
                f"{cls.__name__} missing required typography tokens: {missing}"
            )
