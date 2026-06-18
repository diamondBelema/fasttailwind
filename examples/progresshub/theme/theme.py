"""Aurora theme — modern, rounded, spacious master theme."""
from fasttailwind.contracts import ThemeScheme
from .colors import Colors
from .typography import Typography

class Theme(ThemeScheme):
    colors = Colors()
    typography = Typography()

    # Spacing — generous, modern scale
    space_xs = "1"
    space_sm = "2"
    space_md = "4"
    space_lg = "8"     # was 6 — more breathing room
    space_xl = "12"    # was 8
    space_2xl = "20"   # was 12 — sections feel spacious

    # Border radius — fully rounded, modern
    radius_sm = "rounded-lg"      # was "rounded"
    radius_md = "rounded-xl"      # was "rounded-lg"
    radius_lg = "rounded-2xl"     # was "rounded-xl"
    radius_full = "rounded-full"

    breakpoints = {"sm": "sm", "md": "md", "lg": "lg", "xl": "xl"}

    # ── Component variants ────────────────────────────────────

    button_variants = {
        "primary": (
            "bg-indigo-500 text-white hover:bg-indigo-400 "
            "focus:ring-2 focus:ring-indigo-400 focus:ring-offset-2 "
            "focus:ring-offset-slate-900 transition-all duration-200"
        ),
        "secondary": (
            "bg-slate-800 text-slate-200 hover:bg-slate-700 "
            "focus:ring-2 focus:ring-slate-500 focus:ring-offset-2 "
            "focus:ring-offset-slate-900 transition-all duration-200"
        ),
        "ghost": (
            "bg-transparent text-slate-300 hover:bg-slate-800/50 "
            "focus:ring-2 focus:ring-slate-500 transition-all duration-200"
        ),
        "danger": (
            "bg-rose-500 text-white hover:bg-rose-400 "
            "focus:ring-2 focus:ring-rose-400 focus:ring-offset-2 "
            "focus:ring-offset-slate-900 transition-all duration-200"
        ),
    }

    button_sizes = {
        "sm": "px-4 py-2 text-sm gap-2",
        "md": "px-5 py-2.5 text-base gap-2",
        "lg": "px-6 py-3 text-lg gap-2",
    }

    card_variants = {
        "default": (
            "bg-slate-900 border border-slate-800 "
            "shadow-sm hover:shadow-md transition-shadow duration-300"
        ),
        "elevated": (
            "bg-slate-800 border border-slate-700 "
            "shadow-lg shadow-slate-950/50 "
            "hover:shadow-xl hover:shadow-slate-950/50 "
            "transition-all duration-300 hover:-translate-y-0.5"
        ),
        "ghost": (
            "bg-transparent border border-slate-800/50 "
            "hover:bg-slate-800/30 transition-colors duration-200"
        ),
    }

    badge_variants = {
        "success": (
            "bg-emerald-500/10 text-emerald-400 border border-emerald-500/20"
        ),
        "warning": (
            "bg-amber-500/10 text-amber-400 border border-amber-500/20"
        ),
        "danger": (
            "bg-rose-500/10 text-rose-400 border border-rose-500/20"
        ),
        "info": (
            "bg-sky-500/10 text-sky-400 border border-sky-500/20"
        ),
        "neutral": (
            "bg-slate-500/10 text-slate-400 border border-slate-500/20"
        ),
    }

    input_variants = {
        "default": (
            "bg-slate-800 border border-slate-700 text-slate-100 "
            "placeholder:text-slate-500 "
            "focus:border-indigo-400 focus:ring-2 focus:ring-indigo-400/20 "
            "transition-all duration-200"
        ),
        "error": (
            "bg-slate-800 border border-rose-500 text-slate-100 "
            "focus:border-rose-400 focus:ring-2 focus:ring-rose-400/20 "
            "transition-all duration-200"
        ),
    }

    alert_variants = {
        "success": (
            "bg-emerald-500/5 border border-emerald-500/10 text-emerald-300"
        ),
        "warning": (
            "bg-amber-500/5 border border-amber-500/10 text-amber-300"
        ),
        "danger": (
            "bg-rose-500/5 border border-rose-500/10 text-rose-300"
        ),
        "info": (
            "bg-sky-500/5 border border-sky-500/10 text-sky-300"
        ),
    }
