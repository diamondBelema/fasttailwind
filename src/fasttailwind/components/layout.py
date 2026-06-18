"""Layout components: Row, Column, Grid, Stack."""
from __future__ import annotations
from typing import Any
from htmy import Component, Context, html
from ..utils.cn import cn


class _LayoutBase:
    def __init__(
        self, *children: Any, gap: str | dict[str, str] | None = None,
        align: str | None = None, justify: str | None = None,
        class_: str | None = None, **kwargs: Any,
    ) -> None:
        self._children = children
        self._gap = gap
        self._align = align
        self._justify = justify
        self._class = class_
        self._kwargs = kwargs

    def _resolve_gap(self, resolver: Any) -> str | None:
        if self._gap is None:
            return None
        if isinstance(self._gap, dict):
            return resolver.responsive("gap", self._gap)
        return f"gap-{resolver.spacing(self._gap)}"

    def _build_classes(self, resolver: Any, *extra: str) -> str:
        return cn(
            *extra, self._resolve_gap(resolver),
            f"items-{self._align}" if self._align else None,
            f"justify-{self._justify}" if self._justify else None,
            self._class,
        )


class Row(_LayoutBase):
    """Horizontal flex row."""
    def htmy(self, context: Context) -> Component:
        resolver = context["resolver"]
        classes = self._build_classes(resolver, "flex", "flex-row")
        return html.div(*self._children, class_=classes, **self._kwargs)


class Column(_LayoutBase):
    """Vertical flex column."""
    def htmy(self, context: Context) -> Component:
        resolver = context["resolver"]
        classes = self._build_classes(resolver, "flex", "flex-col")
        return html.div(*self._children, class_=classes, **self._kwargs)


class Stack(_LayoutBase):
    """Vertical stack with sensible defaults (flex-col, full width)."""
    def __init__(
        self, *children: Any, gap: str | dict[str, str] | None = "md",
        align: str | None = None, class_: str | None = None, **kwargs: Any,
    ) -> None:
        super().__init__(*children, gap=gap, align=align, class_=class_, **kwargs)

    def htmy(self, context: Context) -> Component:
        resolver = context["resolver"]
        classes = self._build_classes(resolver, "flex", "flex-col", "w-full")
        return html.div(*self._children, class_=classes, **self._kwargs)


class Grid:
    """CSS Grid layout. Accepts plain value or responsive breakpoint dict for *cols*."""
    def __init__(
        self, *children: Any, cols: int | dict[str, int] = 2,
        gap: str | dict[str, str] | None = "md",
        class_: str | None = None, **kwargs: Any,
    ) -> None:
        self._children = children
        self._cols = cols
        self._gap = gap
        self._class = class_
        self._kwargs = kwargs

    def htmy(self, context: Context) -> Component:
        resolver = context["resolver"]
        col_cls = (
            resolver.responsive("grid-cols", self._cols)
            if isinstance(self._cols, dict)
            else f"grid-cols-{self._cols}"
        )
        gap_cls = None
        if self._gap is not None:
            gap_cls = (
                resolver.responsive("gap", self._gap)
                if isinstance(self._gap, dict)
                else f"gap-{resolver.spacing(self._gap)}"
            )
        classes = cn("grid", col_cls, gap_cls, self._class)
        return html.div(*self._children, class_=classes, **self._kwargs)
