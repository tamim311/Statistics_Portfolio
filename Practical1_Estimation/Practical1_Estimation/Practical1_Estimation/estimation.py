import numpy as np
import pandas as pd

# Load data
data = pd.read_csv("data.csv")
salaries = data["Salary"].values
N = len(salaries)

# Draw random sample of size 10
np.random.seed(42)  # for reproducibility
sample = np.random.choice(salaries, size=10, replace=False)

# Estimates
mean_est = np.mean(sample)
total_est = N * mean_est

# Sample variance
s = np.std(sample, ddof=1)

# Finite population correction
f = len(sample) / N
SE_mean = s * np.sqrt((1 - f) / len(sample))
SE_total = N * SE_mean

# Save results
with open("results.txt", "w") as f:
    f.write(f"Estimated Mean: {mean_est}\n")
    f.write(f"Estimated Total: {total_est}\n")
    f.write(f"SE(Mean): {SE_mean}\n")
    f.write(f"SE(Total): {SE_total}\n")

print("Results saved to results.txt")
