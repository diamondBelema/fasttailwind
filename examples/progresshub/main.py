#!/usr/bin/env python3
"""FastTailwind comprehensive demo — shows every component and customization limit.

Run it:
    cd examples/progresshub
    uv add fastapi uvicorn
    uv run uvicorn main:app --reload

Then open http://localhost:8000 in your browser.
"""
from __future__ import annotations
from fastapi import FastAPI
from fasthx.htmy import HTMY
from htmy import html
from fasttailwind import (
    ThemeContext,
    Button, TextField, Select, Checkbox,
    Card, Badge, Section, Divider,
    Heading, Text, Label, Caption,
    Alert, Spinner, Toast, EmptyState,
    Row, Column, Grid, Stack,
)
from theme import Theme

app = FastAPI()
htmy = HTMY()
theme_ctx = ThemeContext(Theme())


def page_shell(content) -> html.html:
    """Full HTML document with Inter font and Tailwind CDN."""
    return html.html(
        html.head(
            html.title("FastTailwind — Component Showcase"),
            html.meta(charset="utf-8"),
            html.meta(name="viewport", content="width=device-width, initial-scale=1"),
            html.link(
                href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=JetBrains+Mono:wght@400;500&display=swap",
                rel="stylesheet",
            ),
            html.script(src="https://cdn.tailwindcss.com"),
        ),
        html.body(content),
    )


# ═══════════════════════════════════════════════════════════════
# DASHBOARD — shows all components in action
# ═══════════════════════════════════════════════════════════════

def dashboard() -> html.div:
    return theme_ctx.wrap(
        html.div(
            # ── Hero section ─────────────────────────────────────
            html.section(
                html.div(
                    Badge("v0.1.0", variant="info"),
                    class_="mb-4",
                ),
                Heading("FastTailwind", size="3xl"),
                Text(
                    "A theme-agnostic design system for HTMY + FastHX. "
                    "Every component below reads from your theme file.",
                    muted=True,
                    size="lg",
                ),
                class_="mb-12",
            ),

            # ── Typography section ─────────────────────────────
            html.section(
                Heading("Typography", size="2xl"),
                Text("All text sizes, weights, and colors come from the theme.", muted=True),
                html.div(
                    Heading("Heading 3xl — Hero", size="3xl"),
                    Heading("Heading 2xl — Section", size="2xl"),
                    Heading("Heading xl — Subsection", size="xl"),
                    Heading("Heading lg — Card title", size="lg"),
                    Text("Text base — Body copy at default size", size="base"),
                    Text("Text sm — Secondary information", size="sm", muted=True),
                    Text("Text xs — Fine print and captions", size="xs", muted=True),
                    Caption("Caption — Helper text, form hints"),
                    class_="mt-6 space-y-3",
                ),
                class_="mb-12",
            ),

            Divider(margin="lg"),

            # ── Buttons section ──────────────────────────────────
            html.section(
                Heading("Buttons", size="2xl"),
                Text("Variants and sizes defined in theme.button_variants / button_sizes", muted=True),
                html.div(
                    Row(
                        Button("Primary", variant="primary", size="sm"),
                        Button("Primary", variant="primary", size="md"),
                        Button("Primary", variant="primary", size="lg"),
                        gap="sm",
                        align="center",
                    ),
                    Row(
                        Button("Secondary", variant="secondary", size="md"),
                        Button("Ghost", variant="ghost", size="md"),
                        Button("Danger", variant="danger", size="md"),
                        Button("Disabled", variant="primary", size="md", disabled=True),
                        gap="sm",
                        align="center",
                    ),
                    Row(
                        Button("With HTMX", variant="primary", size="md", hx_post="/log", hx_target="#result"),
                        gap="sm",
                        align="center",
                    ),
                    class_="mt-6 space-y-4",
                ),
                html.div(id="result"),
                class_="mb-12",
            ),

            Divider(margin="lg"),

            # ── Cards section ────────────────────────────────────
            html.section(
                Heading("Cards", size="2xl"),
                Text("Three variants: default, elevated (with shadow + hover lift), ghost", muted=True),
                Grid(
                    Card(
                        Heading("Default", size="lg"),
                        Text("Basic card with border and subtle shadow.", muted=True),
                        variant="default",
                        padding="lg",
                    ),
                    Card(
                        Heading("Elevated", size="lg"),
                        Text("Shadow + hover lift animation. Try hovering.", muted=True),
                        variant="elevated",
                        padding="lg",
                    ),
                    Card(
                        Heading("Ghost", size="lg"),
                        Text("Transparent background, subtle border.", muted=True),
                        variant="ghost",
                        padding="lg",
                    ),
                    cols={"base": 1, "md": 3},
                    gap="lg",
                    class_="mt-6",
                ),
                class_="mb-12",
            ),

            Divider(margin="lg"),

            # ── Badges section ───────────────────────────────────
            html.section(
                Heading("Badges", size="2xl"),
                Text("Semantic status indicators with subtle backgrounds", muted=True),
                Row(
                    Badge("Success", variant="success"),
                    Badge("Warning", variant="warning"),
                    Badge("Danger", variant="danger"),
                    Badge("Info", variant="info"),
                    Badge("Neutral", variant="neutral"),
                    gap="sm",
                    align="center",
                    class_="mt-6 flex-wrap",
                ),
                class_="mb-12",
            ),

            Divider(margin="lg"),

            # ── Form inputs section ──────────────────────────────
            html.section(
                Heading("Form Inputs", size="2xl"),
                Text("TextField, Select, Checkbox — all themed via input_variants", muted=True),
                Grid(
                    Card(
                        Label("Project name", html_for="name"),
                        TextField(name="name", placeholder="Enter project name", variant="default"),
                        Caption("This will be visible to your team"),
                        variant="default",
                        padding="lg",
                    ),
                    Card(
                        Label("Priority", html_for="priority"),
                        Select(
                            name="priority",
                            options=[("low", "Low"), ("medium", "Medium"), ("high", "High")],
                            value="medium",
                        ),
                        variant="default",
                        padding="lg",
                    ),
                    Card(
                        Label("Email", html_for="email"),
                        TextField(
                            name="email",
                            type_="email",
                            placeholder="you@example.com",
                            variant="error",
                        ),
                        Caption("Please enter a valid email address"),
                        variant="default",
                        padding="lg",
                    ),
                    Card(
                        Checkbox(name="notify", label="Send me email notifications", checked=True),
                        Checkbox(name="marketing", label="Subscribe to newsletter"),
                        variant="default",
                        padding="lg",
                    ),
                    cols={"base": 1, "md": 2},
                    gap="lg",
                    class_="mt-6",
                ),
                class_="mb-12",
            ),

            Divider(margin="lg"),

            # ── Feedback section ─────────────────────────────────
            html.section(
                Heading("Feedback", size="2xl"),
                Text("Alerts, spinners, toasts, empty states", muted=True),
                Grid(
                    Card(
                        Alert("Your changes have been saved successfully.", variant="success", title="Success"),
                        Alert("Please review your input before continuing.", variant="warning", title="Warning"),
                        Alert("Something went wrong. Please try again.", variant="danger", title="Error"),
                        Alert("Here is some information you might find useful.", variant="info", title="Info"),
                        variant="default",
                        padding="lg",
                    ),
                    Card(
                        html.div(
                            Text("Loading states", size="sm", muted=True),
                            class_="mb-4",
                        ),
                        Row(
                            Spinner(size="sm"),
                            Spinner(size="md"),
                            Spinner(size="lg"),
                            gap="md",
                            align="center",
                        ),
                        html.div(
                            Text("Toast notifications", size="sm", muted=True),
                            class_="mt-6 mb-4",
                        ),
                        Stack(
                            Toast("File uploaded", variant="success"),
                            Toast("Syncing...", variant="info"),
                            Toast("Connection lost", variant="danger"),
                            gap="sm",
                        ),
                        variant="default",
                        padding="lg",
                    ),
                    cols={"base": 1, "md": 2},
                    gap="lg",
                    class_="mt-6",
                ),
                html.div(
                    EmptyState(
                        title="No projects yet",
                        description="Create your first project to get started with tracking.",
                        action=Button("Create project", variant="primary", size="md"),
                        class_="mt-8",
                    ),
                    class_="mt-6",
                ),
                class_="mb-12",
            ),

            Divider(margin="lg"),

            # ── Layout section ───────────────────────────────────
            html.section(
                Heading("Layout", size="2xl"),
                Text("Row, Column, Stack, Grid — all responsive via breakpoint dicts", muted=True),
                Card(
                    Heading("Responsive Grid", size="lg"),
                    Text("Resize your browser. This grid adapts: 1 col → 2 col → 4 col", muted=True),
                    Grid(
                        html.div("1", class_="bg-slate-800 p-4 rounded-xl text-center"),
                        html.div("2", class_="bg-slate-800 p-4 rounded-xl text-center"),
                        html.div("3", class_="bg-slate-800 p-4 rounded-xl text-center"),
                        html.div("4", class_="bg-slate-800 p-4 rounded-xl text-center"),
                        cols={"base": 1, "sm": 2, "lg": 4},
                        gap="md",
                        class_="mt-4",
                    ),
                    variant="elevated",
                    padding="lg",
                    class_="mt-6",
                ),
                Card(
                    Heading("Stack & Row", size="lg"),
                    Text("Vertical stack with gap, horizontal row with alignment", muted=True),
                    Stack(
                        Row(
                            html.div("Left", class_="bg-slate-800 p-4 rounded-xl flex-1 text-center"),
                            html.div("Center", class_="bg-slate-800 p-4 rounded-xl flex-1 text-center"),
                            html.div("Right", class_="bg-slate-800 p-4 rounded-xl flex-1 text-center"),
                            gap="md",
                            align="center",
                        ),
                        Row(
                            Button("Cancel", variant="ghost", size="md"),
                            Button("Save changes", variant="primary", size="md"),
                            gap="sm",
                            justify="end",
                            class_="mt-4",
                        ),
                        gap="md",
                    ),
                    variant="default",
                    padding="lg",
                    class_="mt-6",
                ),
                class_="mb-12",
            ),

            # ── Footer ───────────────────────────────────────────
            html.footer(
                Text("Built with FastTailwind · HTMY · FastHX · Tailwind CSS", muted=True, size="sm"),
                class_="mt-12 pt-8 border-t border-slate-800 text-center",
            ),

            class_="min-h-screen bg-slate-950 text-slate-50 p-6 md:p-12 max-w-6xl mx-auto",
        )
    )


# ═══════════════════════════════════════════════════════════════
# ROUTES
# ═══════════════════════════════════════════════════════════════

@app.get("/", response_model=None)
@htmy.page()
def index() -> html.html:
    """Full component showcase."""
    return page_shell(dashboard())


@app.post("/log", response_model=None)
@htmy.hx()
def log_progress() -> html.div:
    """HTMX endpoint demo."""
    return theme_ctx.wrap(
        Alert("Progress logged successfully!", variant="success", title="Done")
    )


# ── Standalone render ───────────────────────────────────────

async def render_standalone() -> None:
    from htmy import Renderer
    page = index()
    result = await Renderer().render(page)
    print(result)


if __name__ == "__main__":
    import asyncio
    asyncio.run(render_standalone())
