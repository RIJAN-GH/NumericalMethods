# Simple Trapezoidal Rule
def f(x):
    return 1 + x**3

# Input from user
a = float(input("Enter lower limit: "))
b = float(input("Enter upper limit: "))

h = b - a
I = (h / 2) * (f(a) + f(b))

print("Result using Simple Trapezoidal Rule:", I)