"""Tests for contract validation."""
import pytest
from fasttailwind.contracts import ColorScheme, TypographyScheme, ThemeScheme

def test_color_scheme_missing_tokens():
    with pytest.raises(NotImplementedError, match="missing required color tokens"):
        class BadColors(ColorScheme):
            primary = "violet"

def test_color_scheme_complete():
    class GoodColors(ColorScheme):
        primary = "violet"
        secondary = "zinc"
        bg_base = "zinc-950"
        bg_surface = "zinc-900"
        bg_elevated = "zinc-800"
        bg_overlay = "zinc-700"
        text_primary = "zinc-50"
        text_secondary = "zinc-300"
        text_muted = "zinc-500"
        text_disabled = "zinc-600"
        border_default = "zinc-700"
        border_strong = "zinc-500"
        border_focus = "violet-500"
        success = "emerald-500"
        warning = "amber-500"
        danger = "red-500"
        info = "blue-500"
    assert GoodColors.primary == "violet"

def test_typography_scheme_missing_tokens():
    with pytest.raises(NotImplementedError, match="missing required typography tokens"):
        class BadTypography(TypographyScheme):
            font_sans = "font-sans"

def test_theme_scheme_missing_tokens():
    with pytest.raises(NotImplementedError, match="missing required theme attributes"):
        class BadTheme(ThemeScheme):
            colors = None
            typography = None
