import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

# --- Data ---
plotX = np.array([0.03, 0.14, 0.25, 0.34, 0.43, 0.54, 0.65])
plotY = np.array([1.5, 3.1, 4.6, 6.2, 7.8, 9.4, 11.5])


# --- Data selected for linear regression ---
regressionMask = plotX >= 0.30

dataX = plotX[regressionMask]
dataY = plotY[regressionMask]


# --- Linear regression ---
result = stats.linregress(dataX, dataY)

slope = result.slope
intercept = result.intercept
rSquared = result.rvalue ** 2


# --- Regression line ---
dataX_fit = np.linspace(dataX.min(), dataX.max(), 200)
dataY_fit = slope * dataX_fit + intercept


# --- Plot ---
plt.figure(figsize=(8, 6))

plt.scatter(plotX, plotY, 
    color="black", 
    s=20, 
    zorder=3, 
    label="Measurement points"
)

plt.plot(plotX, plotY, 
    color="lightslategray", 
    linewidth=2, 
    zorder=1
)

plt.plot(dataX_fit, dataY_fit, 
    color="blue", 
    linewidth=2, 
    zorder=2, 
    label="Linear regression"
)


# --- Regression equation ---
equationText = (
    f"$U = {slope:.3f}\\,I {intercept:+.3f}$\n"
    f"$R = {slope:.3f}\\,\\mathrm{{\\Omega}}$\n"
    f"$R^2 = {rSquared:.3f}$"
)

plt.text(0.05, 0.94,
    equationText,
    transform=plt.gca().transAxes,
    fontsize=10,
    verticalalignment="top",
    bbox=dict(
        boxstyle="round", 
        facecolor="white", 
        alpha=0.8
    )
)


# --- Plot labels and formatting ---
plt.title("Voltage as a function of current")
plt.xlabel(r"Current $I$ [A]")
plt.ylabel(r"Voltage $U$ [V]")

plt.xlim(left=0)
plt.ylim(bottom=0)

plt.legend(frameon=False, loc="lower right")


# --- Save and display ---
plt.tight_layout()
plt.savefig("LinearRegressionSelectedData.png", dpi=300, bbox_inches="tight")
plt.show()
