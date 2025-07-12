# Least Squares Line Fitting (y = a + bx)
import numpy as np

n = int(input("Enter number of data points: "))
x = np.zeros(n)
y = np.zeros(n)

print("Enter x values:")
for i in range(n):
    x[i] = float(input(f"x[{i}] = "))

print("Enter y values:")
for i in range(n):
    y[i] = float(input(f"y[{i}] = "))

# Least Squares Calculations
sum_x = np.sum(x)
sum_y = np.sum(y)
sum_xy = np.sum(x * y)
sum_x2 = np.sum(x * x)

b = (n * sum_xy - sum_x * sum_y) / (n * sum_x2 - sum_x**2)
a = (sum_y - b * sum_x) / n

print(f"\nBest-fit line: y = {a:.3f} + {b:.3f}x")

xp = float(input("Enter value of x to predict y: "))
yp = a + b * xp
print(f"Predicted value at x = {xp:.3f} is y = {yp:.3f}")
