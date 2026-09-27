import numpy as np
import matplotlib.pyplot as plt

# --- Data ---
data = [1.02, 1.29, 1.65, 1.73, 1.77, 1.81, 1.88, 2.05, 2.11, 2.24, 2.70]


# --- Histogram bins ---
binWidth = 0.5
bins = np.arange(min(data), max(data) + binWidth, binWidth)


# --- Histogram ---
plt.hist(data, 
    bins=bins, 
    color="lightslategray", 
    edgecolor="black"
)


# --- Plot labels and formatting ---
plt.title("Histogram of velocity measurements")
plt.xlabel(r"Velocity $v$ [m/s]")
plt.ylabel(r"Number of measurements $N$")


# --- Save and display ---
plt.tight_layout()
plt.savefig("Histogram.png", dpi=300, bbox_inches="tight")
plt.show()
