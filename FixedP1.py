# Fixed Point Iteration Method for f(x) = x^2 + x - 2

def f(x):
    return x**2 + x - 2

# Rearranged equation: x = g(x) = 2 / (x + 1)
def g(x):
    return 2 / (x + 1)

x0 = float(input("Enter initial guess: "))
tol = float(input("Enter error tolerance: "))
step = 1  

x1 = g(x0)
print("\nStep\t\tx0\t\tx1\t\tf(x1)")

# Print the first iteration step before entering the loop
print(f"{step}\t\t{x0:.6f}\t{x1:.6f}\t{f(x1):.6f}")

while abs(x1 - x0) > tol:
    x0 = x1
    x1 = g(x0)
    step += 1
    print(f"{step}\t\t{x0:.6f}\t{x1:.6f}\t{f(x1):.6f}")

print(f"\nRoot is: {x1:.6f}")
print(f"f(Root) ≈ {f(x1):.6f}")
print(f"Total steps: {step}")
