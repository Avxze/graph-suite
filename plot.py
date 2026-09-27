import matplotlib.pyplot as plt

# --- Data ---
dataX = [0.03, 0.14, 0.25, 0.34, 0.43, 0.54, 0.65]
dataY = [1.5, 3.1, 4.6, 6.2, 7.8, 9.4, 11.5]


# --- Plot ---
plt.scatter(dataX, dataY, 
    color="black", 
    s=20, 
    zorder=2, 
    label="Measurement points"
)

plt.plot(dataX, dataY, 
    color="blue", 
    linewidth=2, 
    zorder=1
)


# --- Plot labels and formatting ---
plt.title("Voltage as a function of current")
plt.xlabel(r"Current $I$ [A]")
plt.ylabel(r"Voltage $U$ [V]")

plt.xlim(left=0)
plt.ylim(bottom=0)

plt.legend(frameon=False)


# --- Save and display ---
plt.tight_layout()
plt.savefig("Plot.png", dpi=300, bbox_inches="tight")
plt.show()
