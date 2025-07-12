# Newton-Raphson Method for f(x) = x * tan(x) - 1

import math

def f(x):
    return x * math.tan(x) - 1

def df(x):
    return x * (1 / math.cos(x))**2 + math.tan(x)

x0 = float(input("Enter initial guess: "))
tol = float(input("Enter error tolerance: "))
step = 1

print("\nStep\t\tx0\t\tx1\t\tf(x1)")

while True:
    if df(x0) == 0:
        print("Zero derivative. No solution found.")
        break

    x1 = x0 - f(x0) / df(x0)
    f1 = f(x1)

    print(f"{step}\t\t{x0:.6f}\t{x1:.6f}\t{f1:.6f}")

    if abs(f1) < tol:
        break

    x0 = x1
    step += 1

print(f"\nThe root is: {x1:.6f}")
print(f"Total steps: {step}")
