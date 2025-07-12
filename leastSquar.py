# Least Squares Line Fitting (y = a + bx) without NumPy

n = int(input("Enter number of data points: "))
x = []
y = []

print("Enter x values:")
for i in range(n):
    val = float(input(f"x[{i}] = "))
    x.append(val)

print("Enter y values:")
for i in range(n):
    val = float(input(f"y[{i}] = "))
    y.append(val)

# Manual calculations
sum_x = sum(x)
sum_y = sum(y)
sum_xy = sum(x[i] * y[i] for i in range(n))
sum_x2 = sum(x[i] * x[i] for i in range(n))

# Least Squares formula
b = (n * sum_xy - sum_x * sum_y) / (n * sum_x2 - sum_x ** 2)
a = (sum_y - b * sum_x) / n

print(f"\nBest-fit line: y = {a:.3f} + {b:.3f}x")

xp = float(input("Enter value of x to predict y: "))
yp = a + b * xp
print(f"Predicted value at x = {xp:.3f} is y = {yp:.3f}")
