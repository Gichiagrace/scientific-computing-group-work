# Task S: Random Numbers and Monte Carlo Methods

## 1. Mathematical Concept

Monte Carlo methods use repeated random sampling to estimate probabilities or solve problems involving uncertainty. The more simulations performed, the more reliable the estimated probability generally becomes.

## 2. Original Program: Server Overload Risk

**File name:** `code/Task_20_monte_carlo.py`

### Input Values

- Server capacity: 1000 units
- Mean demand: 850 units
- Standard deviation: 120 units
- Number of simulations: 100,000
- Random seed: 42

### Mathematical Operations

The program generates random server-demand values using a normal distribution. It checks whether each demand value exceeds server capacity.

The overload probability is calculated as:

`Overload probability = Number of overload cases / Total simulations`

### Output and Interpretation

- Estimated overload probability: **10.6160%**
- Number of overload cases: **10,616 out of 100,000**

This means that approximately 10.62% of the simulated demand scenarios exceeded server capacity.

The graph shows how the estimated probability changes as the number of simulations increases. It gradually becomes more stable as more simulations are performed.

## 3. Parameter Modification

The mean demand was increased from 850 to 900 units while keeping the other parameters unchanged.

### Modified Output

- Estimated overload probability: **20.2210%**
- Number of overload cases: **20,221 out of 100,000**

### Interpretation

Increasing the average demand increased the probability of server overload from 10.6160% to 20.2210%. This shows that higher incoming demand increases the risk of exceeding server capacity.

## 4. Real-World Application: Water Shortage Risk

The original program was modified to estimate the probability of daily water demand exceeding the