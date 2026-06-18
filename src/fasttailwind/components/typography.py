"""Typography components: Heading, Text, Label, Caption."""
from __future__ import annotations
from typing import Any
from htmy import Component, Context, html
from ..utils.cn import cn


class Heading:
    """Semantic heading with theme-driven size."""
    TAG_MAP = {"xs": "h4", "sm": "h4", "base": "h3", "lg": "h3", "xl": "h2", "2xl": "h2", "3xl": "h1"}

    def __init__(self, text: str, *, size: str = "xl", class_: str | None = None, **kwargs: Any) -> None:
        self._text = text
        self._size = size
        self._class = class_
        self._kwargs = kwargs

    def htmy(self, context: Context) -> Component:
        resolver = context["resolver"]
        theme = context["theme"]
        size_cls = resolver.resolve(f"typography.size_{self._size}")
        tag = self.TAG_MAP.get(self._size, "h2")
        classes = cn(
            size_cls, theme.typography.font_sans, theme.typography.weight_bold,
            theme.typography.leading_tight, f"text-{theme.colors.text_primary}", self._class,
        )
        return getattr(html, tag)(self._text, class_=classes, **self._kwargs)


class Text:
    """Body text with optional muted styling."""
    def __init__(self, text: str, *, size: str = "base", muted: bool = False,
                 class_: str | None = None, **kwargs: Any) -> None:
        self._text = text
        self._size = size
        self._muted = muted
        self._class = class_
        self._kwargs = kwargs

    def htmy(self, context: Context) -> Component:
        resolver = context["resolver"]
        theme = context["theme"]
        size_cls = resolver.resolve(f"typography.size_{self._size}")
        color_cls = f"text-{theme.colors.text_muted}" if self._muted else f"text-{theme.colors.text_secondary}"
        classes = cn(size_cls, color_cls, theme.typography.font_sans, theme.typography.leading_normal, self._class)
        return html.p(self._text, class_=classes, **self._kwargs)


class Label:
    """Form label."""
    def __init__(self, text: str, *, html_for: str | None = None,
                 class_: str | None = None, **kwargs: Any) -> None:
        self._text = text
        self._html_for = html_for
        self._class = class_
        self._kwargs = kwargs

    def htmy(self, context: Context) -> Component:
        theme = context["theme"]
        classes = cn("block text-sm font-medium", f"text-{theme.colors.text_primary}", self._class)
        attrs = {"for": self._html_for} if self._html_for else {}
        return html.label(self._text, class_=classes, **attrs, **self._kwargs)


class Caption:
    """Small caption/helper text."""
    def __init__(self, text: str, *, class_: str | None = None, **kwargs: Any) -> None:
        self._text = text
        self._class = class_
        self._kwargs = kwargs

    def htmy(self, context: Context) -> Component:
        theme = context["theme"]
        classes = cn("text-xs", f"text-{theme.colors.text_muted}", self._class)
        return html.p(self._text, class_=classes, **self._kwargs)
