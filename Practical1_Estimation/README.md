# Practical 1: Estimation of Mean and Total

## Problem Statement
We have a population of 30 employees with their monthly salaries (in thousand Taka).  
A simple random sample of size 10 is selected using random numbers.  
We estimate:
1. Average monthly salary
2. Total monthly salary of all 30 employees
3. Standard error of the estimated average
4. Standard error of the estimated total

## Methodology
- Sampling method: Simple Random Sampling (without replacement).
- Random numbers were used to select IDs.
- Formulas applied:
  - Mean: \(\bar{y} = \frac{1}{n}\sum y_i\)
  - Total: \(Y = N \cdot \bar{y}\)
  - Standard Error of Mean: \(SE(\bar{y}) = \sqrt{\frac{1-f}{n}} \cdot s\)
  - Standard Error of Total: \(SE(Y) = N \cdot SE(\bar{y})\)

## Code
See `estimation.py` for implementation in Python.

## Results
- Estimated Mean: …
- Estimated Total: …
- SE(Mean): …
- SE(Total): …

## Learning Outcome
This exercise demonstrates how sample-based estimates can be used to infer population parameters and highlights the role of standard error in measuring reliability.
