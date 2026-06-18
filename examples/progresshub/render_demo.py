#!/usr/bin/env python3
"""Standalone demo — renders a complete HTML page to stdout.

Run it:
    cd examples/progresshub
    uv run python render_demo.py > demo.html
    # Then open demo.html in your browser
"""
from __future__ import annotations
import asyncio
from htmy import Renderer, html
from fasttailwind import ThemeContext, Button, Card, Grid, Heading, Text, Badge
from theme import Theme

async def main() -> None:
    theme_ctx = ThemeContext(Theme())

    # The dashboard content
    content = theme_ctx.wrap(
        html.div(
            Heading("Progress Hub", size="3xl"),
            Text("You are 3 days ahead of pace.", muted=True),
            Grid(
                Card(
                    Heading("Predicted completion", size="lg"),
                    Text("June 24 — 3 days ahead", muted=True),
                    Badge("On track", variant="success"),
                    variant="elevated",
                    padding="lg",
                ),
                Card(
                    Heading("Today's target", size="lg"),
                    Text("2,000 words", muted=True),
                    Button("Log progress", variant="primary", size="md"),
                    variant="default",
                    padding="lg",
                ),
                cols={"base": 1, "md": 2},
                gap="md",
            ),
            class_="min-h-screen bg-zinc-950 p-8 text-zinc-50",
        )
    )

    # FULL HTML document with Tailwind CSS
    page = html.html(
        html.head(
            html.title("Progress Hub — FastTailwind Demo"),
            html.meta(charset="utf-8"),
            html.meta(name="viewport", content="width=device-width, initial-scale=1"),
            # Tailwind CSS CDN — THIS makes the classes work
            html.script(src="https://cdn.tailwindcss.com"),
        ),
        html.body(content),
    )

    result = await Renderer().render(page)
    print(result)

if __name__ == "__main__":
    asyncio.run(main())
