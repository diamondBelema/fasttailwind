"""Tests for the TokenResolver."""
import pytest
from fasttailwind.resolver import TokenResolver
from fasttailwind.contracts import ColorScheme, TypographyScheme, ThemeScheme

class TestColors(ColorScheme):
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

class TestTypography(TypographyScheme):
    font_sans = "font-sans"
    font_mono = "font-mono"
    size_xs = "text-xs"
    size_sm = "text-sm"
    size_base = "text-base"
    size_lg = "text-lg"
    size_xl = "text-xl"
    size_2xl = "text-2xl"
    size_3xl = "text-3xl"
    weight_normal = "font-normal"
    weight_medium = "font-medium"
    weight_bold = "font-bold"
    leading_tight = "leading-tight"
    leading_normal = "leading-normal"
    leading_relaxed = "leading-relaxed"

class TestTheme(ThemeScheme):
    colors = TestColors()
    typography = TestTypography()
    space_xs = "1"
    space_sm = "2"
    space_md = "4"
    space_lg = "6"
    space_xl = "8"
    space_2xl = "12"
    radius_sm = "rounded"
    radius_md = "rounded-lg"
    radius_lg = "rounded-xl"
    radius_full = "rounded-full"
    breakpoints = {"sm": "sm", "md": "md", "lg": "lg", "xl": "xl"}
    button_variants = {"primary": "bg-violet-600 text-white"}
    button_sizes = {"md": "px-4 py-2"}
    card_variants = {"default": "bg-zinc-900"}
    badge_variants = {}
    input_variants = {}
    alert_variants = {}

@pytest.fixture
def resolver():
    return TokenResolver(TestTheme())

def test_resolve_simple(resolver):
    assert resolver.resolve("space_md") == "4"

def test_resolve_nested(resolver):
    assert resolver.resolve("colors.bg_surface") == "zinc-900"
    assert resolver.resolve("typography.size_lg") == "text-lg"

def test_resolve_missing(resolver):
    with pytest.raises(ValueError):
        resolver.resolve("nonexistent")

def test_variant(resolver):
    assert resolver.variant("button", "primary") == "bg-violet-600 text-white"
    assert resolver.variant("button", "missing") == ""

def test_size(resolver):
    assert resolver.size("button", "sm") == ""
    assert resolver.size("button", "md") == "px-4 py-2"

def test_responsive(resolver):
    result = resolver.responsive("grid-cols", {"base": 1, "md": 2, "lg": 3})
    assert result == "grid-cols-1 md:grid-cols-2 lg:grid-cols-3"

def test_spacing(resolver):
    assert resolver.spacing("md") == "4"

def test_radius(resolver):
    assert resolver.radius("lg") == "rounded-xl"
