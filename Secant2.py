# Secant Method for f(x) = 4*sin(x) - e^x

from math import sin, e

def f(x):
    return 4 * sin(x) - e**x

x0 = float(input("Enter initial guess x0: "))
x1 = float(input("Enter next guess x1: "))
tol = float(input("Enter error tolerance: "))

step = 1
print("\nStep\t\tx0\t\tx1\t\tx2\t\tf(x2)")
while True:
    f0 = f(x0)
    f1 = f(x1)

    if f1 - f0 == 0:
        print("Division by zero error!")
        break

    x2 = x1 - f1 * (x1 - x0) / (f1 - f0)
    f2 = f(x2)
    print(f"{step}\t\t{x0:.6f}\t{x1:.6f}\t{x2:.6f}\t{f2:.6f}")

    if abs(f2) < tol:
        break

    x0, x1 = x1, x2
    step += 1

print(f"\nRoot is: {x2:.6f}")
print(f"Total steps: {step}")
