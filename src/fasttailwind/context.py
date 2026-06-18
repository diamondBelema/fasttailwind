"""HTMY context integration for theme propagation."""
from __future__ import annotations
from typing import Any
from htmy import Component, ComponentType, Context, html
from .contracts.theme import ThemeScheme
from .resolver import TokenResolver


class ThemeContext:
    """HTMY context provider that injects theme and resolver into the render tree."""

    def __init__(self, theme: ThemeScheme) -> None:
        self._theme = theme
        self._resolver = TokenResolver(theme)

    @property
    def theme(self) -> ThemeScheme:
        return self._theme

    @property
    def resolver(self) -> TokenResolver:
        return self._resolver

    def htmy_context(self) -> Context:
        return {"theme": self._theme, "resolver": self._resolver}

    def wrap(self, *children: ComponentType) -> "_ThemeContextWrapper":
        """Wrap children in a context provider component."""
        return _ThemeContextWrapper(self, *children)


class _ThemeContextWrapper:
    """Internal wrapper that acts as both context provider and component."""

    def __init__(self, ctx: ThemeContext, *children: ComponentType) -> None:
        self._ctx = ctx
        self._children = children

    def htmy_context(self) -> Context:
        return self._ctx.htmy_context()

    def htmy(self, context: Context) -> Component:
        return self._children
