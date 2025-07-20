# Simple Simpson 3-8 Rule
def f(x):
    return 1 + x**3

a = float(input("Enter lower limit: "))
b = float(input("Enter upper limit: "))

h = (b - a) / 3
x1 = a + h
x2 = a + 2 * h
I = (3 * h / 8) * (f(a) + 3 * f(x1) + 3 * f(x2) + f(b))

print("Simple Simpson's 3/8 result:", I)
