# Newton's Divided Difference Interpolation
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

#  Create divided difference table
dd = np.zeros((n, n))
dd[:, 0] = y

# for j in range(1, n):
#     for i in range(n - j):
#         dd[i][j] = (dd[i + 1][j - 1] - dd[i][j - 1]) / (x[i + j] - x[i])

xp = float(input("Enter interpolation point: "))

# Apply Newton's formula
yp = dd[0][0]
term = 1.0
for i in range(1, n):
    term *= (xp - x[i - 1])
    yp += dd[0][i] * term

# print("\nDivided Difference Table:")
# for i in range(n):
#     for j in range(n - i):
#         print(f"{dd[i][j]:.5f}", end="\t")
#     print()

print(f"\nInterpolated value at x = {xp:.3f} is {yp:.5f}")
