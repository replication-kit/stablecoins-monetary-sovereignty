from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


# Figure 1 for:
# "Stablecoins and Monetary Sovereignty: A Theory of Functional Fragmentation"
#
# Illustration:
#   - standard logistic distribution
#   - network-effect parameter alpha = 6
#
# The figure is monochrome for journal submission.
# Solid branches are locally stable; the dashed branch is locally unstable.


ALPHA = 6.0

REPO_ROOT = Path(__file__).resolve().parents[1]
OUTPUT_DIR = REPO_ROOT / "figures"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)


def F(y):
    """Standard logistic CDF."""
    return 1.0 / (1.0 + np.exp(-y))


def z_of_y(y):
    """Return z in the parametric equilibrium representation."""
    return y - ALPHA * F(y)


# Turning points satisfy ALPHA * f(y) = 1.
# For the standard logistic distribution, f(y) = F(y) * (1 - F(y)).
disc = 1.0 - 4.0 / ALPHA
q_low = (1.0 - np.sqrt(disc)) / 2.0
q_high = (1.0 + np.sqrt(disc)) / 2.0

y_L = np.log(q_low / (1.0 - q_low))
y_H = np.log(q_high / (1.0 - q_high))

z_bar = z_of_y(y_L)
z_under = z_of_y(y_H)


# Parametric equilibrium curve
y = np.linspace(-8.0, 8.0, 2000)
x = F(y)
z = z_of_y(y)

mask_low = y < y_L
mask_mid = (y >= y_L) & (y <= y_H)
mask_high = y > y_H


fig, ax = plt.subplots(figsize=(7.6, 5.2))

# Stable and unstable equilibrium branches
ax.plot(z[mask_low], x[mask_low], color="black", linewidth=2.0)
ax.plot(
    z[mask_mid],
    x[mask_mid],
    color="black",
    linestyle="--",
    linewidth=1.8,
)
ax.plot(z[mask_high], x[mask_high], color="black", linewidth=2.0)

# Critical values
ax.axvline(z_under, color="black", linestyle=":", linewidth=1.2)
ax.axvline(z_bar, color="black", linestyle=":", linewidth=1.2)

# Branch labels
low_idx = np.where(mask_low)[0][260]
mid_indices = np.where(mask_mid)[0]
mid_idx = mid_indices[len(mid_indices) // 2]
high_idx = np.where(mask_high)[0][-260]

ax.text(
    z[low_idx],
    x[low_idx] + 0.035,
    r"$x^L$",
    ha="center",
    va="bottom",
    fontsize=11,
)
ax.text(
    z[mid_idx],
    x[mid_idx] + 0.055,
    r"$x^M$",
    ha="center",
    va="bottom",
    fontsize=11,
)
ax.text(
    z[high_idx],
    x[high_idx] - 0.055,
    r"$x^H$",
    ha="center",
    va="top",
    fontsize=11,
)

# Axis labels
ax.set_xlabel(
    r"Fundamental relative advantage of the external channel, $z$",
    labelpad=12,
)
ax.set_ylabel(r"Equilibrium externalization rate, $x$")

ax.set_xlim(min(z) + 0.25, max(z) - 0.25)
ax.set_ylim(0.0, 1.0)
ax.grid(False)

# Academic-style frame
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)

# Place the critical-value labels at the same level as numeric tick labels.
default_ticks = [
    t for t in ax.get_xticks()
    if ax.get_xlim()[0] <= t <= ax.get_xlim()[1]
]

# Remove nearby numeric tick labels to avoid overlap.
min_sep = 0.55
kept_ticks = [
    t for t in default_ticks
    if abs(t - z_under) > min_sep and abs(t - z_bar) > min_sep
]

all_ticks = sorted(kept_ticks + [z_under, z_bar])

tick_labels = []
for t in all_ticks:
    if np.isclose(t, z_under):
        tick_labels.append("z̲")
    elif np.isclose(t, z_bar):
        tick_labels.append("z̄")
    else:
        tick_labels.append(f"{t:g}")

ax.set_xticks(all_ticks)
ax.set_xticklabels(tick_labels)

fig.subplots_adjust(bottom=0.17)

fig.savefig(
    OUTPUT_DIR / "figure1_multiple_equilibria_bw_v4.png",
    dpi=300,
    bbox_inches="tight",
)
fig.savefig(
    OUTPUT_DIR / "figure1_multiple_equilibria_bw_v4.eps",
    format="eps",
    bbox_inches="tight",
)

plt.close(fig)
