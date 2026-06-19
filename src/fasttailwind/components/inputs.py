"""Input components: Button, TextField, Select, Checkbox."""

from __future__ import annotations
from typing import Any
from htmy import Component, Context, html
from ..utils.cn import cn


class Button:
    """Theme-driven button with HTMX support. Any ``hx_*`` kwarg forwards to the HTML element."""

    def __init__(
        self,
        label: str,
        *,
        variant: str = "primary",
        size: str = "md",
        radius: str = "md",
        disabled: bool = False,
        class_: str | None = None,
        **kwargs: Any,
    ) -> None:
        self._label = label
        self._variant = variant
        self._size = size
        self._radius = radius
        self._disabled = disabled
        self._class = class_
        self._kwargs = kwargs

    def htmy(self, context: Context) -> Component:
        resolver = context["resolver"]
        variant_cls = resolver.variant("button", self._variant)
        size_cls = resolver.size("button", self._size)
        classes = cn(
            "inline-flex items-center justify-center font-medium transition-colors "
            "focus:outline-none focus:ring-2 focus:ring-offset-2 disabled:opacity-50 disabled:cursor-not-allowed",
            resolver.radius(self._radius),
            variant_cls,
            size_cls,
            self._class,
        )
        return html.button(
            self._label,
            class_=classes,
            disabled="disabled" if self._disabled else None,
            **self._kwargs,
        )


class TextField:
    """Text input with theme-driven variants."""

    def __init__(
        self,
        *,
        name: str,
        type_: str = "text",
        placeholder: str | None = None,
        value: str | None = None,
        variant: str = "default",
        radius: str = "md",
        disabled: bool = False,
        class_: str | None = None,
        **kwargs: Any,
    ) -> None:
        self._name = name
        self._type = type_
        self._placeholder = placeholder
        self._value = value
        self._variant = variant
        self._radius = radius
        self._disabled = disabled
        self._class = class_
        self._kwargs = kwargs

    def htmy(self, context: Context) -> Component:
        resolver = context["resolver"]
        variant_cls = resolver.variant("input", self._variant)
        classes = cn(
            "block w-full shadow-sm transition-colors focus:outline-none focus:ring-2",
            resolver.radius(self._radius),
            variant_cls,
            self._class,
        )
        return html.input_(
            class_=classes,
            type=self._type,
            name=self._name,
            placeholder=self._placeholder,
            value=self._value,
            disabled="disabled" if self._disabled else None,
            **self._kwargs,
        )


class Select:
    """Dropdown select with theme-driven styling."""

    def __init__(
        self,
        *,
        name: str,
        options: list[tuple[str, str]],
        value: str | None = None,
        variant: str = "default",
        radius: str = "md",
        disabled: bool = False,
        class_: str | None = None,
        **kwargs: Any,
    ) -> None:
        self._name = name
        self._options = options
        self._value = value
        self._variant = variant
        self._radius = radius
        self._disabled = disabled
        self._class = class_
        self._kwargs = kwargs

    def htmy(self, context: Context) -> Component:
        resolver = context["resolver"]
        variant_cls = resolver.variant("input", self._variant)
        classes = cn(
            "block w-full shadow-sm transition-colors focus:outline-none focus:ring-2",
            resolver.radius(self._radius),
            variant_cls,
            self._class,
        )
        opts = []
        for opt_val, opt_label in self._options:
            sel = {"selected": "selected"} if opt_val == self._value else {}
            opts.append(html.option(opt_label, value=opt_val, **sel))
        return html.select(
            *opts,
            class_=classes,
            name=self._name,
            disabled="disabled" if self._disabled else None,
            **self._kwargs,
        )


class Checkbox:
    """Theme-styled checkbox."""

    def __init__(
        self,
        *,
        name: str,
        label: str | None = None,
        checked: bool = False,
        disabled: bool = False,
        class_: str | None = None,
        **kwargs: Any,
    ) -> None:
        self._name = name
        self._label = label
        self._checked = checked
        self._disabled = disabled
        self._class = class_
        self._kwargs = kwargs

    def htmy(self, context: Context) -> Component:
        theme = context["theme"]
        resolver = context["resolver"]
        checkbox = html.input_(
            class_=cn(
                "h-4 w-4 focus:ring-2",
                resolver.radius("sm"),
                f"border-{theme.colors.border_default}",
                f"text-{theme.colors.primary}-500 focus:ring-{theme.colors.primary}-500",
                self._class,
            ),
            type="checkbox",
            name=self._name,
            checked="checked" if self._checked else None,
            disabled="disabled" if self._disabled else None,
            **self._kwargs,
        )
        if self._label:
            return html.label(
                checkbox,
                html.span(
                    self._label, class_=f"text-{theme.colors.text_secondary} text-sm"
                ),
                class_="inline-flex items-center space-x-2 cursor-pointer",
            )
        return checkbox
