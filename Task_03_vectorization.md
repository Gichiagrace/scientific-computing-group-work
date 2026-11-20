# Task 3: Mathematical Functions and Vectorization

## 1. Mathematical Concept
Vectorization is applying a mathematical operation to many values at once instead of using a loop for each value. NumPy supports vectorized calculations, making them simpler and usually faster.

For example:

\[
y_i=\sin^2(x_i)+\cos^2(x_i)=1
\]

## 2. Inputs and Mathematical Operations
The original program uses:
- `latency_ms`: One million randomly generated network latency readings between 5 and 250 milliseconds.
- `1000.0`: Converts milliseconds into seconds.
- `**2`: Squares each converted latency value.
- `timeit`: Measures the execution time of the loop and vectorized methods.

## 3. Parameter Change
The number of readings can be increased from `1_000_000` to `2_000_000`.

This means the program processes twice as many measurements. It will require more processing time and memory, while vectorization still avoids writing a Python loop for every reading.

## 4. Output Interpretation
The program displays the first five squared latency values, execution times for both methods and their approximate speed-up.

A higher speed-up means the vectorized method performs the calculation faster than the loop method.

## 5. Modified Real-World Application
**Application: Electricity consumption analysis**

Assumptions:
- Power readings are collected in watts.
- Readings range between 100 and 5,000 watts.
- The readings are converted into kilowatts and squared.

```python
import numpy as np
import matplotlib.pyplot as plt

rng = np.random.default_rng(42)
power_watts = rng.uniform(100, 5000, 100_000)

power_kw = power_watts / 1000
squared_power = power_kw ** 2

print("First five readings in kW:", power_kw[:5])
print("First five squared values:", squared_power[:5])
print("Average power:", np.mean(power_kw), "kW")

plt.plot(power_kw[:100])
plt.xlabel("Measurement")
plt.ylabel("Power (kW)")
plt.title("Electricity Consumption Analysis")
plt.grid(True)
plt.show()
```

**Interpretation:** The program converts power readings from watts to kilowatts, squares the values and calculates average power consumption. The graph shows how power readings change across the first 100 measurements.

## Conclusion
Vectorization allows NumPy to process large amounts of numerical data efficiently, reducing the need for repeated Python loops.