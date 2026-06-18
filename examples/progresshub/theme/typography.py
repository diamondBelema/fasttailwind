"""Aurora theme — modern typography with Inter font."""
from fasttailwind.contracts import TypographyScheme

class Typography(TypographyScheme):
    # Inter font family (loaded via Google Fonts in main.py)
    font_sans = "font-['Inter',system-ui,sans-serif]"
    font_mono = "font-['JetBrains_Mono',monospace]"

    # Size scale — slightly larger, more breathing room
    size_xs = "text-xs"
    size_sm = "text-sm"
    size_base = "text-base"
    size_lg = "text-lg"
    size_xl = "text-xl"
    size_2xl = "text-2xl"
    size_3xl = "text-4xl"  # bumped up for hero headings

    # Weights — modern, not too heavy
    weight_normal = "font-normal"
    weight_medium = "font-medium"
    weight_bold = "font-semibold"  # semibold instead of bold for modern feel

    # Line heights — airy
    leading_tight = "leading-snug"
    leading_normal = "leading-relaxed"
    leading_relaxed = "leading-loose"
