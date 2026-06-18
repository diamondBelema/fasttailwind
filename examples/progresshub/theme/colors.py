"""Aurora theme — modern, soft, rounded color scheme."""
from fasttailwind.contracts import ColorScheme

class Colors(ColorScheme):
    # Brand palette — soft indigo/violet family
    primary = "indigo"
    secondary = "slate"
    accent = "teal"

    # Surfaces — slightly warmer than pure slate
    bg_base = "slate-950"
    bg_surface = "slate-900"
    bg_elevated = "slate-800"
    bg_overlay = "slate-700"

    # Text — high contrast but not harsh
    text_primary = "slate-50"
    text_secondary = "slate-300"
    text_muted = "slate-400"
    text_disabled = "slate-600"

    # Borders — subtle, modern
    border_default = "slate-700"
    border_strong = "slate-500"
    border_focus = "indigo-400"

    # Status — softer, less aggressive
    success = "emerald-400"
    warning = "amber-400"
    danger = "rose-400"
    info = "sky-400"
