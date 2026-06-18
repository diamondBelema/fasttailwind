"""Tests for safelist generation."""
from fasttailwind.safelist import safelist
from tests.test_resolver import TestTheme

def test_safelist_includes_variants():
    classes = safelist(TestTheme())
    assert "bg-violet-600" in classes
    assert "text-white" in classes

def test_safelist_includes_colors():
    classes = safelist(TestTheme())
    assert "zinc-900" in classes
    assert "bg-zinc-900" in classes

def test_safelist_is_sorted():
    classes = safelist(TestTheme())
    assert classes == sorted(classes)
