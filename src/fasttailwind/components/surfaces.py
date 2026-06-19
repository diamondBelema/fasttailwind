"""Surface components: Card, Badge, Section, Divider."""
from __future__ import annotations
from typing import Any
from htmy import Component, Context, html
from ..utils.cn import cn


class Card:
    """Content container with theme-driven variants."""
    def __init__(
        self, *children: Any, variant: str = "default",
        padding: str | dict[str, str] | None = None,
        radius: str = "lg",
        class_: str | None = None, **kwargs: Any,
    ) -> None:
        self._children = children
        self._variant = variant
        self._padding = padding
        self._radius = radius
        self._class = class_
        self._kwargs = kwargs

    def htmy(self, context: Context) -> Component:
        resolver = context["resolver"]
        variant_cls = resolver.variant("card", self._variant)
        pad_cls = None
        if self._padding is not None:
            pad_cls = (
                resolver.responsive("p", self._padding)
                if isinstance(self._padding, dict)
                else f"p-{resolver.spacing(self._padding)}"
            )
        radius_cls = resolver.radius(self._radius) if self._radius else None
        classes = cn(radius_cls, variant_cls, pad_cls, self._class)
        return html.div(*self._children, class_=classes, **self._kwargs)


class Badge:
    """Status badge with semantic variants."""
    def __init__(self, label: str, *, variant: str = "neutral",
                 class_: str | None = None, **kwargs: Any) -> None:
        self._label = label
        self._variant = variant
        self._class = class_
        self._kwargs = kwargs

    def htmy(self, context: Context) -> Component:
        resolver = context["resolver"]
        variant_cls = resolver.variant("badge", self._variant)
        classes = cn(
            "inline-flex items-center px-2.5 py-0.5 rounded-full text-xs font-medium",
            variant_cls, self._class,
        )
        return html.span(self._label, class_=classes, **self._kwargs)


class Section:
    """Semantic section wrapper with optional padding and background."""
    def __init__(
        self, *children: Any, padding: str | dict[str, str] | None = None,
        bg: str | None = None, class_: str | None = None, **kwargs: Any,
    ) -> None:
        self._children = children
        self._padding = padding
        self._bg = bg
        self._class = class_
        self._kwargs = kwargs

    def htmy(self, context: Context) -> Component:
        resolver = context["resolver"]
        pad_cls = None
        if self._padding is not None:
            pad_cls = (
                resolver.responsive("p", self._padding)
                if isinstance(self._padding, dict)
                else f"p-{resolver.spacing(self._padding)}"
            )
        bg_cls = f"bg-{resolver.resolve(f'colors.bg_{self._bg}')}" if self._bg else None
        classes = cn(pad_cls, bg_cls, self._class)
        return html.section(*self._children, class_=classes, **self._kwargs)


class Divider:
    """Horizontal divider line."""
    def __init__(self, *, margin: str | None = "md",
                 class_: str | None = None, **kwargs: Any) -> None:
        self._margin = margin
        self._class = class_
        self._kwargs = kwargs

    def htmy(self, context: Context) -> Component:
        resolver = context["resolver"]
        theme = context["theme"]
        margin_cls = f"my-{resolver.spacing(self._margin)}" if self._margin else None
        classes = cn("w-full border-t", f"border-{theme.colors.border_default}", margin_cls, self._class)
        return html.hr(class_=classes, **self._kwargs)
