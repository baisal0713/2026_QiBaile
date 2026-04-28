"""
Generate visual reference materials for the ID4 Interaction Model.

Outputs:
  1. pipeline-diagram.svg/png  — the atom pipeline with path branching
  2. curves-reference.svg/png  — all 11 curve shapes, grouped
  3. cheat-sheet.svg/png       — one-page printable reference

Uses matplotlib only (no external dependencies beyond numpy).
"""

import math
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
from matplotlib.gridspec import GridSpec
from pathlib import Path

OUT_DIR = Path(r"D:\Projects Unity\MD4_2026_Mavrodiev_Develop"
               r"\Docs\Interactive Design 4\Interaction Model\visuals")
OUT_DIR.mkdir(exist_ok=True)

# ═══════════════════════════════════════════════════════════════
#  SHARED STYLE
# ═══════════════════════════════════════════════════════════════

BG         = "#FAFAFA"
DARK       = "#2C3E50"
ACCENT     = "#2980B9"
ACCENT2    = "#E74C3C"
GREEN      = "#27AE60"
AMBER      = "#F39C12"
LIGHT_GRAY = "#ECF0F1"
MID_GRAY   = "#BDC3C7"

PATH_COLORS = {"A": "#2980B9", "B": "#27AE60", "C": "#F39C12", "D": "#E74C3C"}
PATH_BG     = {"A": "#DCEEFB", "B": "#D5F5E3", "C": "#FEF5E7", "D": "#FADBD8"}

plt.rcParams.update({
    "font.family": "sans-serif",
    "font.sans-serif": ["Segoe UI", "Calibri", "Arial", "Helvetica"],
    "font.size": 10,
    "axes.facecolor": BG,
    "figure.facecolor": "#FFFFFF",
    "axes.edgecolor": MID_GRAY,
    "axes.grid": False,
})


# ═══════════════════════════════════════════════════════════════
#  CURVE FUNCTIONS
# ═══════════════════════════════════════════════════════════════

x = np.linspace(0, 1, 200)

def linear(x):       return x
def ease_in(x):      return x**2
def ease_out(x):     return 1 - (1 - x)**2
def ease_inout(x):   return np.where(x < 0.5, 2*x**2, 1 - (-2*x + 2)**2 / 2)
def inverse(x):      return 1 - x
def s_curve(x):      return 3*x**2 - 2*x**3

def burst(x):
    with np.errstate(divide='ignore', invalid='ignore'):
        y = np.where(x <= 0, 0, (x / 0.1) * np.exp(1 - x / 0.1))
    return np.minimum(y, 1.5)

def swell(x):        return np.sin(np.pi * x)

def snap_tail(x):    return np.exp(-4 * x)

def overshoot(x):
    with np.errstate(divide='ignore', invalid='ignore'):
        y = np.where(x <= 0, 0, 1.4 * (x / 0.15) * np.exp(1 - x / 0.15))
    return np.minimum(y, 1.5)

def spike(x):
    return np.where(x < 0.05, x / 0.05, np.maximum(0, (1 - x) / 0.95))


MAPPING_CURVES = [
    ("Linear",      linear,    "y = x"),
    ("Ease-in",     ease_in,   "y = x\u00b2"),
    ("Ease-out",    ease_out,  "y = 1-(1-x)\u00b2"),
    ("Ease-in-out", ease_inout,"smooth step"),
    ("Inverse",     inverse,   "y = 1-x"),
    ("S-curve",     s_curve,   "y = 3x\u00b2-2x\u00b3"),
]

RESPONSE_CURVES = [
    ("Burst",       burst,      "fast peak, fast decay"),
    ("Swell",       swell,      "gradual rise and fall"),
    ("Snap + tail", snap_tail,  "instant peak, slow decay"),
    ("Overshoot",   overshoot,  "peak past target, settle"),
    ("Spike",       spike,      "sharp triangle peak"),
]


# ═══════════════════════════════════════════════════════════════
#  1. PIPELINE DIAGRAM
# ═══════════════════════════════════════════════════════════════

def draw_pipeline():
    fig, ax = plt.subplots(figsize=(14, 7))
    ax.set_xlim(0, 14)
    ax.set_ylim(0, 7)
    ax.axis("off")
    fig.patch.set_facecolor("#FFFFFF")

    # Title
    ax.text(7, 6.6, "THE INTERACTION ATOM", fontsize=18, fontweight="bold",
            ha="center", va="top", color=DARK)
    ax.text(7, 6.2, "Input \u2192 Signal \u2192 Relationship \u2192 Shape \u2192 Output",
            fontsize=11, ha="center", va="top", color=MID_GRAY)

    # ── Pipeline boxes ──
    boxes = [
        (1.0, 4.2, 2.0, 1.2, "INPUT",    DARK,   "#FFFFFF",
         "Proximity\nGaze\nContact\nVelocity\nButton\nSlider\nTime"),
        (3.8, 4.2, 1.6, 1.2, "SIGNAL",   DARK,   LIGHT_GRAY,
         "Continuous\nor Binary"),
        (6.2, 4.2, 2.2, 1.2, "RELATIONSHIP", DARK, LIGHT_GRAY,
         "Bound\nor Unbound"),
        (9.2, 4.2, 2.2, 1.2, "SHAPE",    DARK,   LIGHT_GRAY,
         "Curve\nRange\nEnvelope"),
        (12.0, 4.2, 1.6, 1.2, "OUTPUT",  DARK,   "#FFFFFF",
         "Light\nMaterial\nSound\nParticles\nEnvironment\nCamera"),
    ]

    for bx, by, bw, bh, title, tc, bg, sub in boxes:
        rect = FancyBboxPatch((bx, by), bw, bh, boxstyle="round,pad=0.1",
                              facecolor=bg, edgecolor=tc, linewidth=1.5)
        ax.add_patch(rect)
        ax.text(bx + bw/2, by + bh - 0.15, title, fontsize=11, fontweight="bold",
                ha="center", va="top", color=tc)
        ax.text(bx + bw/2, by + bh - 0.45, sub, fontsize=7, ha="center", va="top",
                color="#7F8C8D", linespacing=1.3)

    # ── Arrows between boxes ──
    arrow_style = "simple,head_width=8,head_length=6"
    for x1, x2 in [(3.0, 3.8), (5.4, 6.2), (8.4, 9.2), (11.4, 12.0)]:
        ax.annotate("", xy=(x2, 4.8), xytext=(x1, 4.8),
                    arrowprops=dict(arrowstyle="->", color=MID_GRAY, lw=2))

    # ── 2x2 Mode Matrix below ──
    mx, my = 3.5, 0.3  # matrix origin
    mw, mh = 7.0, 3.2
    cell_w, cell_h = mw / 2, mh / 2

    # Title
    ax.text(mx + mw/2, my + mh + 0.3, "INTERACTION MODES",
            fontsize=13, fontweight="bold", ha="center", color=DARK)

    # Column headers
    ax.text(mx + cell_w * 0.5, my + mh + 0.05, "BOUND",
            fontsize=10, fontweight="bold", ha="center", color=DARK)
    ax.text(mx + cell_w * 1.5, my + mh + 0.05, "UNBOUND",
            fontsize=10, fontweight="bold", ha="center", color=DARK)

    # Row headers
    ax.text(mx - 0.15, my + cell_h * 1.5, "CONTINUOUS",
            fontsize=9, fontweight="bold", ha="right", va="center",
            color=DARK, rotation=90)
    ax.text(mx - 0.15, my + cell_h * 0.5, "BINARY",
            fontsize=9, fontweight="bold", ha="right", va="center",
            color=DARK, rotation=90)

    cells = [
        # col, row, path, name, example, active_params
        (0, 1, "A", "Tracking",
         "Proximity \u2192 Light intensity",
         "Curve \u00b7 Range \u00b7 Attack \u00b7 Release"),
        (1, 1, "B", "Threshold Trigger",
         "Gaze duration hits 3s \u2192 material dissolves",
         "Curve \u00b7 Threshold \u00b7 Duration"),
        (0, 0, "C", "Switch",
         "Enter zone \u2192 Light ON / OFF",
         "Attack \u00b7 Release"),
        (1, 0, "D", "One-Shot",
         "Button press \u2192 play animation",
         "Curve \u00b7 Duration"),
    ]

    for col, row, path, name, example, params in cells:
        cx = mx + col * cell_w
        cy = my + row * cell_h
        rect = FancyBboxPatch((cx + 0.05, cy + 0.05),
                              cell_w - 0.1, cell_h - 0.1,
                              boxstyle="round,pad=0.08",
                              facecolor=PATH_BG[path],
                              edgecolor=PATH_COLORS[path],
                              linewidth=1.5)
        ax.add_patch(rect)

        ax.text(cx + cell_w/2, cy + cell_h - 0.2,
                name,
                fontsize=9, fontweight="bold", ha="center", va="top",
                color=PATH_COLORS[path])
        ax.text(cx + cell_w/2, cy + cell_h - 0.55,
                example, fontsize=7.5, ha="center", va="top", color="#555555")
        ax.text(cx + cell_w/2, cy + 0.22,
                params, fontsize=6.5, ha="center", va="bottom",
                color="#888888", style="italic")

    # ── Connection lines from RELATIONSHIP box down to matrix ──
    ax.annotate("", xy=(mx + mw/2, my + mh + 0.15),
                xytext=(7.3, 4.2),
                arrowprops=dict(arrowstyle="->", color=MID_GRAY, lw=1.5,
                                connectionstyle="arc3,rad=0"))

    fig.tight_layout(pad=0.5)
    fig.savefig(OUT_DIR / "pipeline-diagram.svg", bbox_inches="tight", dpi=150)
    fig.savefig(OUT_DIR / "pipeline-diagram.png", bbox_inches="tight", dpi=200)
    plt.close(fig)
    print("  pipeline-diagram.svg/png")


# ═══════════════════════════════════════════════════════════════
#  2. CURVES REFERENCE CARD
# ═══════════════════════════════════════════════════════════════

def draw_curves():
    fig = plt.figure(figsize=(14, 7))
    fig.patch.set_facecolor("#FFFFFF")

    # Title
    fig.text(0.5, 0.97, "CURVE SHAPES REFERENCE",
             fontsize=16, fontweight="bold", ha="center", va="top", color=DARK)

    # Two rows: mapping curves (top), response curves (bottom)
    gs = GridSpec(2, 6, figure=fig, hspace=0.5, wspace=0.35,
                 top=0.90, bottom=0.08, left=0.05, right=0.95)

    # ── Row 1: Mapping curves (Bound modes — Input to Output) ──
    fig.text(0.02, 0.93, "MAPPING CURVES  (Bound modes: Input \u2192 Output)",
             fontsize=10, fontweight="bold", color=ACCENT, va="bottom")

    for i, (name, func, formula) in enumerate(MAPPING_CURVES):
        ax = fig.add_subplot(gs[0, i])
        y = func(x)
        ax.plot(x, y, color=ACCENT, linewidth=2.5)
        ax.axhline(y=1, color=MID_GRAY, linewidth=0.5, linestyle="--", alpha=0.5)
        ax.set_xlim(0, 1)
        ax.set_ylim(-0.05, 1.15)
        ax.set_title(name, fontsize=9, fontweight="bold", color=DARK, pad=4)
        ax.set_xlabel(formula, fontsize=7, color="#999999", labelpad=2)
        ax.set_xticks([0, 1])
        ax.set_yticks([0, 1])
        ax.tick_params(labelsize=7, colors="#AAAAAA")
        ax.set_facecolor("#FAFAFA")
        for spine in ax.spines.values():
            spine.set_color(MID_GRAY)
            spine.set_linewidth(0.5)

    # ── Row 2: Response curves (Unbound modes — Time to Output) ──
    fig.text(0.02, 0.46, "RESPONSE CURVES  (Unbound modes: Time \u2192 Output)",
             fontsize=10, fontweight="bold", color=ACCENT2, va="bottom")

    for i, (name, func, desc) in enumerate(RESPONSE_CURVES):
        ax = fig.add_subplot(gs[1, i])
        y = func(x)
        ax.plot(x, y, color=ACCENT2, linewidth=2.5)
        ax.axhline(y=1, color=MID_GRAY, linewidth=0.5, linestyle="--", alpha=0.5)
        ax.set_xlim(0, 1)
        ax.set_ylim(-0.05, 1.55)
        ax.set_title(name, fontsize=9, fontweight="bold", color=DARK, pad=4)
        ax.set_xlabel(desc, fontsize=7, color="#999999", labelpad=2)
        ax.set_xticks([0, 1])
        ax.set_yticks([0, 1])
        ax.tick_params(labelsize=7, colors="#AAAAAA")
        ax.set_facecolor("#FAFAFA")
        for spine in ax.spines.values():
            spine.set_color(MID_GRAY)
            spine.set_linewidth(0.5)

    # Fill the empty 6th cell with a note
    ax_note = fig.add_subplot(gs[1, 5])
    ax_note.axis("off")
    ax_note.text(0.5, 0.5,
                 "Custom\n\nUse\nAnimationCurve\nin Unity",
                 fontsize=8, ha="center", va="center",
                 color="#AAAAAA", style="italic")

    fig.savefig(OUT_DIR / "curves-reference.svg", bbox_inches="tight", dpi=150)
    fig.savefig(OUT_DIR / "curves-reference.png", bbox_inches="tight", dpi=200)
    plt.close(fig)
    print("  curves-reference.svg/png")


# ═══════════════════════════════════════════════════════════════
#  3. ONE-PAGE CHEAT SHEET
# ═══════════════════════════════════════════════════════════════

def draw_cheat_sheet():
    fig = plt.figure(figsize=(11, 15))  # ~A4 portrait-ish
    fig.patch.set_facecolor("#FFFFFF")

    # ── TITLE ──
    fig.text(0.5, 0.98, "INTERACTION ATOM \u2014 CHEAT SHEET",
             fontsize=20, fontweight="bold", ha="center", va="top", color=DARK)
    fig.text(0.5, 0.965, "Interactive Design 4  |  Reference Card",
             fontsize=10, ha="center", va="top", color=MID_GRAY)

    # Layout: 5 sections stacked vertically
    # Section 1: Pipeline (0.87 - 0.95)
    # Section 2: 4 Paths (0.64 - 0.86)
    # Section 3: Curves  (0.38 - 0.63)
    # Section 4: Parameters (0.22 - 0.37)
    # Section 5: Coupling Quality (0.03 - 0.21)

    # ════════ SECTION 1: PIPELINE ════════

    fig.text(0.05, 0.945, "THE PIPELINE",
             fontsize=12, fontweight="bold", color=DARK)

    ax_pipe = fig.add_axes([0.05, 0.875, 0.9, 0.06])
    ax_pipe.set_xlim(0, 10)
    ax_pipe.set_ylim(0, 1)
    ax_pipe.axis("off")

    pipe_items = [
        (0.3, "INPUT",     DARK,    "what triggers it"),
        (2.3, "SIGNAL",    "#7F8C8D","Cont / Binary"),
        (4.3, "RELATIONSHIP","#7F8C8D","Bound / Unbound"),
        (6.5, "SHAPE",     "#7F8C8D","Curve + Range\n+ Envelope"),
        (8.7, "OUTPUT",    DARK,    "what changes"),
    ]

    for px, label, color, sub in pipe_items:
        rect = FancyBboxPatch((px, 0.1), 1.6, 0.8, boxstyle="round,pad=0.05",
                              facecolor=LIGHT_GRAY, edgecolor=color, linewidth=1.5)
        ax_pipe.add_patch(rect)
        ax_pipe.text(px + 0.8, 0.65, label, fontsize=8, fontweight="bold",
                     ha="center", va="center", color=color)
        ax_pipe.text(px + 0.8, 0.3, sub, fontsize=6, ha="center", va="center",
                     color="#999999", linespacing=1.2)

    for x1 in [1.9, 3.9, 6.1, 8.3]:
        ax_pipe.annotate("", xy=(x1 + 0.3, 0.5), xytext=(x1, 0.5),
                         arrowprops=dict(arrowstyle="->", color=MID_GRAY, lw=1.5))

    # ════════ SECTION 2: INTERACTION MODES ════════

    fig.text(0.05, 0.855, "INTERACTION MODES",
             fontsize=12, fontweight="bold", color=DARK)

    # 2x2 matrix
    path_data = [
        # (grid_col, grid_row, path, title, example, params, killed)
        (0, 0, "A", "Tracking",
         "Proximity \u2192 Light intensity",
         "Curve \u00b7 Input Range \u00b7 Output Range\nAttack \u00b7 Release",
         "Duration"),
        (1, 0, "B", "Threshold Trigger",
         "Gaze duration hits 3s \u2192 material dissolves",
         "Curve \u00b7 Threshold \u00b7 Output Range\nDuration",
         "Input Range \u00b7 Attack \u00b7 Release"),
        (0, 1, "C", "Switch",
         "Enter zone \u2192 Light ON / OFF",
         "Output Range \u00b7 Attack \u00b7 Release",
         "Curve \u00b7 Input Range \u00b7 Duration"),
        (1, 1, "D", "One-Shot",
         "Button press \u2192 play animation",
         "Curve \u00b7 Output Range \u00b7 Duration",
         "Input Range \u00b7 Attack \u00b7 Release"),
    ]

    matrix_x, matrix_y = 0.12, 0.665
    cell_w, cell_h = 0.38, 0.085

    # Column/Row headers
    fig.text(matrix_x + cell_w * 0.5, 0.845, "BOUND",
             fontsize=9, fontweight="bold", ha="center", color=DARK)
    fig.text(matrix_x + cell_w * 1.5 + 0.02, 0.845, "UNBOUND",
             fontsize=9, fontweight="bold", ha="center", color=DARK)
    fig.text(matrix_x - 0.03, matrix_y + cell_h * 1.5, "CONTINUOUS",
             fontsize=8, fontweight="bold", ha="center", va="center",
             color=DARK, rotation=90)
    fig.text(matrix_x - 0.03, matrix_y + cell_h * 0.5, "BINARY",
             fontsize=8, fontweight="bold", ha="center", va="center",
             color=DARK, rotation=90)

    for col, row, path, title, example, params, killed in path_data:
        cx = matrix_x + col * (cell_w + 0.02)
        cy = matrix_y + (1 - row) * (cell_h + 0.01)

        ax_cell = fig.add_axes([cx, cy, cell_w, cell_h])
        ax_cell.set_xlim(0, 1)
        ax_cell.set_ylim(0, 1)
        ax_cell.axis("off")

        rect = FancyBboxPatch((0.02, 0.02), 0.96, 0.96,
                              boxstyle="round,pad=0.03",
                              facecolor=PATH_BG[path],
                              edgecolor=PATH_COLORS[path],
                              linewidth=1.5)
        ax_cell.add_patch(rect)

        ax_cell.text(0.5, 0.88, title,
                     fontsize=9, fontweight="bold", ha="center", va="top",
                     color=PATH_COLORS[path])
        ax_cell.text(0.5, 0.63, example,
                     fontsize=7.5, ha="center", va="top", color="#555555")
        ax_cell.text(0.5, 0.38, params,
                     fontsize=6.5, ha="center", va="top", color="#666666",
                     linespacing=1.3)
        ax_cell.text(0.5, 0.08, f"x  {killed}",
                     fontsize=5.5, ha="center", va="bottom",
                     color="#CC0000", alpha=0.5)

    # ════════ SECTION 3: CURVES ════════

    fig.text(0.05, 0.645, "CURVE SHAPES",
             fontsize=12, fontweight="bold", color=DARK)

    fig.text(0.05, 0.625, "Mapping (Bound: Input\u2192Output)",
             fontsize=8, fontweight="bold", color=ACCENT)

    gs_map = GridSpec(1, 6, figure=fig, left=0.05, right=0.95,
                      bottom=0.505, top=0.615, wspace=0.3)

    for i, (name, func, formula) in enumerate(MAPPING_CURVES):
        ax = fig.add_subplot(gs_map[0, i])
        y = func(x)
        ax.plot(x, y, color=ACCENT, linewidth=2)
        ax.axhline(y=1, color=MID_GRAY, linewidth=0.3, linestyle="--", alpha=0.4)
        ax.set_xlim(0, 1)
        ax.set_ylim(-0.05, 1.15)
        ax.set_title(name, fontsize=7, fontweight="bold", color=DARK, pad=2)
        ax.set_xticks([])
        ax.set_yticks([])
        for spine in ax.spines.values():
            spine.set_color(MID_GRAY)
            spine.set_linewidth(0.3)

    fig.text(0.05, 0.49, "Response (Unbound: Time\u2192Output)",
             fontsize=8, fontweight="bold", color=ACCENT2)

    gs_resp = GridSpec(1, 6, figure=fig, left=0.05, right=0.95,
                       bottom=0.385, top=0.48, wspace=0.3)

    for i, (name, func, desc) in enumerate(RESPONSE_CURVES):
        ax = fig.add_subplot(gs_resp[0, i])
        y = func(x)
        ax.plot(x, y, color=ACCENT2, linewidth=2)
        ax.axhline(y=1, color=MID_GRAY, linewidth=0.3, linestyle="--", alpha=0.4)
        ax.set_xlim(0, 1)
        ax.set_ylim(-0.05, 1.55)
        ax.set_title(name, fontsize=7, fontweight="bold", color=DARK, pad=2)
        ax.set_xticks([])
        ax.set_yticks([])
        for spine in ax.spines.values():
            spine.set_color(MID_GRAY)
            spine.set_linewidth(0.3)

    # 6th cell: note
    ax_note = fig.add_subplot(gs_resp[0, 5])
    ax_note.axis("off")
    ax_note.text(0.5, 0.5, "Custom\ncurve", fontsize=7, ha="center", va="center",
                 color="#BBBBBB", style="italic")

    # ════════ SECTION 4: PARAMETERS ════════

    fig.text(0.05, 0.365, "PARAMETERS BY MODE",
             fontsize=12, fontweight="bold", color=DARK)

    ax_params = fig.add_axes([0.05, 0.235, 0.9, 0.12])
    ax_params.axis("off")

    # Table
    param_rows = [
        ("Parameter",  "Tracking (Cont+Bound)", "Thr. Trigger (Cont+Unbound)",
         "Switch (Bin+Bound)", "One-Shot (Bin+Unbound)"),
        ("Curve",      "+  Input>Output",     "+  Time>Output",
         "--  killed",                "+  Time>Output"),
        ("Input Range","+  min / max",        ">  Threshold only",
         "--  killed",                "--  killed"),
        ("Attack",     "+  smoothing in",     "--  in curve",
         "+  transition>ON",          "--  in curve"),
        ("Release",    "+  smoothing out",    "--  in curve",
         "+  transition>OFF",         "--  killed"),
        ("Duration",   "--  continuous",      "+  play length",
         "--  continuous",            "+  play length"),
    ]

    col_x = [0.0, 0.13, 0.35, 0.55, 0.77]
    col_colors = ["#555555", PATH_COLORS["A"], PATH_COLORS["B"],
                  PATH_COLORS["C"], PATH_COLORS["D"]]

    for ri, row_data in enumerate(param_rows):
        y_pos = 1.0 - ri * 0.17
        is_header = ri == 0
        for ci, val in enumerate(row_data):
            color = col_colors[ci] if not is_header else DARK
            weight = "bold" if (is_header or ci == 0) else "normal"
            fontsize = 7.5 if is_header else 7
            alpha = 0.4 if "--" in val else 1.0
            ax_params.text(col_x[ci], y_pos, val,
                          fontsize=fontsize, fontweight=weight,
                          color=color, alpha=alpha, va="center",
                          transform=ax_params.transAxes)

    # ════════ SECTION 5: COUPLING QUALITY ════════

    fig.text(0.05, 0.215, "COUPLING QUALITY VOCABULARY",
             fontsize=12, fontweight="bold", color=DARK)
    fig.text(0.05, 0.197, "How does the interaction feel? Describe using these pairs:",
             fontsize=8, color="#999999")

    ax_qual = fig.add_axes([0.05, 0.04, 0.9, 0.15])
    ax_qual.set_xlim(0, 10)
    ax_qual.set_ylim(0, 5)
    ax_qual.axis("off")

    qualities = [
        ("Eager",      "Reluctant",   "attack speed",     "fast attack",     "slow attack"),
        ("Crisp",      "Lingering",   "release speed",    "fast release",    "slow release"),
        ("Attentive",  "Indifferent", "proportionality",  "continuous map",  "threshold/binary"),
        ("Precise",    "Forgiving",   "range sensitivity", "narrow input",   "wide input range"),
        ("Alive",      "Still",       "oscillation",      "pulsing/modulated","steady/static"),
    ]

    for i, (left, right, dimension, left_desc, right_desc) in enumerate(qualities):
        y = 4.2 - i * 0.95

        # Left label
        ax_qual.text(0.8, y, left, fontsize=10, fontweight="bold",
                     ha="right", va="center", color=ACCENT)
        ax_qual.text(0.8, y - 0.3, left_desc, fontsize=6,
                     ha="right", va="center", color="#AAAAAA")

        # Spectrum line
        ax_qual.plot([1.0, 5.0], [y, y], color=MID_GRAY, linewidth=2, solid_capstyle="round")
        ax_qual.plot(1.0, y, 'o', color=ACCENT, markersize=6)
        ax_qual.plot(5.0, y, 'o', color=ACCENT2, markersize=6)

        # Center label
        ax_qual.text(3.0, y + 0.25, dimension, fontsize=6.5,
                     ha="center", va="bottom", color="#999999", style="italic")

        # Right label
        ax_qual.text(5.2, y, right, fontsize=10, fontweight="bold",
                     ha="left", va="center", color=ACCENT2)
        ax_qual.text(5.2, y - 0.3, right_desc, fontsize=6,
                     ha="left", va="center", color="#AAAAAA")

        # Second column (compact parameter hint)
        hints = [
            "Tracking: smoothing  |  Switch: transition speed",
            "Tracking: smoothing  |  Switch: transition speed",
            "Tracking: curve shape  |  Thr./One-Shot: response shape",
            "Tracking: input range width  |  Switch: zone size",
            "Time input  |  LFO modulation",
        ]
        ax_qual.text(9.5, y, hints[i], fontsize=5.5,
                     ha="right", va="center", color="#CCCCCC")

    fig.savefig(OUT_DIR / "cheat-sheet.svg", bbox_inches="tight", dpi=150)
    fig.savefig(OUT_DIR / "cheat-sheet.png", bbox_inches="tight", dpi=200)
    plt.close(fig)
    print("  cheat-sheet.svg/png")


# ═══════════════════════════════════════════════════════════════
#  RUN
# ═══════════════════════════════════════════════════════════════

if __name__ == "__main__":
    print(f"Output dir: {OUT_DIR}")
    print("Generating...")
    draw_pipeline()
    draw_curves()
    draw_cheat_sheet()
    print("Done.")
