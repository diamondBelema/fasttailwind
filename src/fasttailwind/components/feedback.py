"""Feedback components: Toast, Spinner, Alert, EmptyState."""
from __future__ import annotations
from typing import Any
from htmy import Component, Context, html
from ..utils.cn import cn


class Alert:
    """Contextual alert message with semantic variants."""
    def __init__(self, message: str, *, variant: str = "info", title: str | None = None,
                 class_: str | None = None, **kwargs: Any) -> None:
        self._message = message
        self._variant = variant
        self._title = title
        self._class = class_
        self._kwargs = kwargs

    def htmy(self, context: Context) -> Component:
        resolver = context["resolver"]
        variant_cls = resolver.variant("alert", self._variant)
        classes = cn("rounded-lg p-4", variant_cls, self._class)
        children = []
        if self._title:
            children.append(html.h3(self._title, class_="text-sm font-medium mb-1"))
        children.append(html.p(self._message, class_="text-sm"))
        return html.div(*children, class_=classes, role="alert", **self._kwargs)


class Spinner:
    """Loading spinner."""
    SIZE_MAP = {"sm": "h-4 w-4", "md": "h-6 w-6", "lg": "h-8 w-8", "xl": "h-12 w-12"}

    def __init__(self, *, size: str = "md", class_: str | None = None, **kwargs: Any) -> None:
        self._size = size
        self._class = class_
        self._kwargs = kwargs

    def htmy(self, context: Context) -> Component:
        theme = context["theme"]
        size_cls = self.SIZE_MAP.get(self._size, self.SIZE_MAP["md"])
        classes = cn(
            "animate-spin rounded-full border-2 border-current border-t-transparent",
            size_cls, f"text-{theme.colors.text_muted}", self._class,
        )
        return html.div(class_=classes, role="status", aria_label="Loading", **self._kwargs)


class Toast:
    """Toast notification."""
    def __init__(self, message: str, *, variant: str = "info",
                 class_: str | None = None, **kwargs: Any) -> None:
        self._message = message
        self._variant = variant
        self._class = class_
        self._kwargs = kwargs

    def htmy(self, context: Context) -> Component:
        resolver = context["resolver"]
        variant_cls = resolver.variant("alert", self._variant)
        classes = cn("rounded-lg p-4 shadow-lg", variant_cls, self._class)
        return html.div(self._message, class_=classes, role="status", **self._kwargs)


class EmptyState:
    """Empty state placeholder."""
    def __init__(self, *, title: str, description: str | None = None, icon: Any | None = None,
                 action: Any | None = None, class_: str | None = None, **kwargs: Any) -> None:
        self._title = title
        self._description = description
        self._icon = icon
        self._action = action
        self._class = class_
        self._kwargs = kwargs

    def htmy(self, context: Context) -> Component:
        theme = context["theme"]
        children = []
        if self._icon:
            children.append(
                html.div(self._icon, class_=f"mx-auto h-12 w-12 text-{theme.colors.text_muted}")
            )
        children.append(
            html.h3(self._title, class_=f"mt-2 text-sm font-semibold text-{theme.colors.text_primary}")
        )
        if self._description:
            children.append(
                html.p(self._description, class_=f"mt-1 text-sm text-{theme.colors.text_muted}")
            )
        if self._action:
            children.append(html.div(self._action, class_="mt-6"))
        classes = cn("text-center py-12", self._class)
        return html.div(*children, class_=classes, **self._kwargs)
