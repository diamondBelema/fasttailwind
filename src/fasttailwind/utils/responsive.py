"""Breakpoint dict → prefixed Tailwind class string converter."""
from __future__ import annotations
from typing import Any


def responsive(prop: str, values: dict[str, Any]) -> str:
    """Convert a breakpoint dict to prefixed Tailwind class strings."""
    classes: list[str] = []
    for bp, val in values.items():
        prefix = f"{bp}:" if bp != "base" else ""
        classes.append(f"{prefix}{prop}-{val}")
    return " ".join(classes)
