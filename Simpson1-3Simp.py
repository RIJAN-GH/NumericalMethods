# Simple Simpson 1/3 Rule
def f(x):
    return 1 + x**3

# Input from user
a = float(input("Enter lower limit: "))
b = float(input("Enter upper limit: "))

h = (b - a)/2
I = h/3 * (f(a) + 4*f((a+b)/2) + f(b))

print("Simple Simpson 1/3 result:", I)