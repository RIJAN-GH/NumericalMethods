def f(x):
    return 1 + x**3

# Input from user
a = float(input("Enter lower limit: "))
b = float(input("Enter upper limit: "))
n = int(input("Enter number of strips (n): "))

h = (b - a) / n
I = f(a) + f(b)
for i in range(1, n):
    I += 2*f(a + i*h)

I = (h / 2) * I

print("Result using Composite Trapezoidal Rule:", I)