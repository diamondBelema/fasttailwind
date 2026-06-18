"""Tests for the cn() utility."""
from fasttailwind.utils.cn import cn

def test_basic_merge():
    assert cn("px-4", "bg-zinc-900") == "px-4 bg-zinc-900"

def test_conditional():
    assert cn("px-4", "opacity-50" if True else None) == "px-4 opacity-50"
    assert cn("px-4", "opacity-50" if False else None) == "px-4"

def test_dict_form():
    assert cn({"w-full": True, "hidden": False}) == "w-full"
    assert cn({"w-full": True, "hidden": True}) == "w-full hidden"

def test_mixed():
    assert cn("base", {"cond1": True, "cond2": False}, "tail") == "base cond1 tail"

def test_falsy_values_dropped():
    assert cn("a", None, "", 0, False, "b") == "a b"
