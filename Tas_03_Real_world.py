
import numpy as np
import matplotlib.pyplot as plt

# Simulated electricity consumption readings in watts
rng = np.random.default_rng(42)
power_watts = rng.uniform(100, 5000, 100_000)

# Convert watts to kilowatts
power_kw = power_watts / 1000

# Square the converted values
squared_power = power_kw ** 2

# Calculate average consumption
average_power = np.mean(power_kw)

print("First five readings in watts:", power_watts[:5])
print("First five readings in kilowatts:", power_kw[:5])
print("First five squared values:", squared_power[:5])
print(f"Average power consumption: {average_power:.2f} kW")

# Visualize electricity consumption
plt.plot(power_kw[:100])
plt.xlabel("Measurement")
plt.ylabel("Power (kW)")
plt.title("Electricity Consumption Analysis")
plt.grid(True)
plt.show()
