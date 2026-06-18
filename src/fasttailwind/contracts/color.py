"""Color scheme contract — defines the shape of a user's color theme."""
from __future__ import annotations


class ColorScheme:
    """Base class for color themes. Subclass and set all required attributes."""

    _required = [
        "primary", "secondary",
        "bg_base", "bg_surface", "bg_elevated", "bg_overlay",
        "text_primary", "text_secondary", "text_muted", "text_disabled",
        "border_default", "border_strong", "border_focus",
        "success", "warning", "danger", "info",
    ]

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        missing = [a for a in cls._required if not hasattr(cls, a)]
        if missing:
            raise NotImplementedError(
                f"{cls.__name__} missing required color tokens: {missing}"
            )
