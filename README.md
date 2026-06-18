# FastTailwind

A theme-agnostic design system layer for [HTMY](https://github.com/volfpeter/htmy) + [FastHX](https://github.com/volfpeter/fasthx).

## Quick Start

```bash
# 1. Create project
uv init --lib myapp
cd myapp

# 2. Install dependencies
uv add fasttailwind htmy fasthx

# 3. Generate a theme
python -c "from fasttailwind.utils import generate_theme; generate_theme('myapp/theme', primary='violet', secondary='zinc', tertiary='emerald')"

# 4. Write your app (see examples/)
# 5. Run it
uv run python main.py
```

## ⚠️ You Need Tailwind CSS

FastTailwind outputs Tailwind CSS **class names** in HTML. But the browser needs the actual CSS rules to make them work. You have two options:

### Option A: Tailwind CDN (easiest, for development)

Add this to your HTML `<head>`:

```python
html.script(src="https://cdn.tailwindcss.com")
```

### Option B: Compiled Tailwind CSS (production)

1. Install Tailwind CSS:
   ```bash
   npm install -D tailwindcss
   npx tailwindcss init
   ```

2. Configure `tailwind.config.js`:
   ```javascript
   export default {
       content: ["./src/**/*.py"],
       safelist: [], // generate from your theme
       theme: { extend: {} },
       plugins: [],
   }
   ```

3. Generate the safelist:
   ```bash
   uv run python -c "from fasttailwind import safelist; from myapp.theme import Theme; import json; print(json.dumps(safelist(Theme())))" > safelist.json
   ```

4. Build CSS:
   ```bash
   npx tailwindcss -i ./src/input.css -o ./static/output.css --watch
   ```

5. Serve the CSS file as a static asset.

## Running the Examples

### Standalone render (no server)
```bash
cd examples/progresshub
uv run python render_demo.py > demo.html
# Open demo.html in your browser
```

### FastAPI + FastHX server
```bash
cd examples/progresshub
uv add fastapi uvicorn
uv run uvicorn main:app --reload
# Open http://localhost:8000
```

### Tests
```bash
uv add --dev pytest pytest-asyncio
uv run pytest tests/ -v
```

## FastHX v3 + FastAPI v3 API

Routes returning HTMY components need `response_model=None`:

```python
from fastapi import FastAPI
from fasthx.htmy import HTMY
from htmy import html
from fasttailwind import ThemeContext, Button, Card, Grid, Heading, Text
from myapp.theme import Theme

app = FastAPI()
htmy = HTMY()
theme_ctx = ThemeContext(Theme())

@app.get("/", response_model=None)
@htmy.page()
def index() -> html.html:
    return html.html(
        html.head(
            html.title("My App"),
            html.script(src="https://cdn.tailwindcss.com"),  # ← Tailwind CDN
        ),
        html.body(
            theme_ctx.wrap(
                html.div(
                    Heading("Hello", size="3xl"),
                    Text("Welcome to FastTailwind."),
                    Button("Get started", variant="primary"),
                    class_="min-h-screen bg-zinc-950 p-8 text-zinc-50",
                )
            )
        ),
    )
```

## Architecture

```
Your code
├── theme.py      → spacing, radius, breakpoints, component variants
├── colors.py     → palette + semantic tokens
└── typography.py → font families, sizes, weights

FastTailwind core
├── ThemeContext    → HTMY context provider
├── TokenResolver   → tokens → Tailwind classes
├── cn()            → conditional class merger
└── safelist()      → Tailwind purge helper

Components
├── Layout    → Row, Column, Grid, Stack
├── Surfaces  → Card, Badge, Section, Divider
├── Inputs    → Button, TextField, Select, Checkbox
├── Feedback  → Toast, Spinner, Alert, EmptyState
└── Typography → Heading, Text, Label, Caption
```

## License

MIT
