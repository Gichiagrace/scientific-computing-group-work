
import numpy as np
import matplotlib.pyplot as plt

rng = np.random.default_rng(42)

available_water = 1000.0
mean_demand = 850.0
std_demand = 120.0
N = 100_000

# Generate random daily water demand
demand = rng.normal(mean_demand, std_demand, N)

# Identify days with water shortages
shortage = demand > available_water
shortage_probability = shortage.mean()

print(f"Estimated shortage probability: {shortage_probability:.4%}")
print(f"Shortage cases: {shortage.sum()} out of {N}")

# Running probability
running_probability = np.cumsum(shortage) / np.arange(1, N + 1)

indices = np.unique(
    np.logspace(1, np.log10(N), 200).astype(int)
) - 1

plt.semilogx(indices + 1, running_probability[indices])
plt.xlabel("Number of simulations")
plt.ylabel("Estimated water shortage probability")
plt.title("Monte Carlo Estimate of Water Shortage Risk")
plt.grid(True)
plt.show()
