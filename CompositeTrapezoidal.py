def f(x):
    return 1 + x**3

def composite_trapezoidal(a, b, n):
    h = (b - a) / n
    sum_fx = f(a) + f(b)
    for i in range(1, n):
        x = a + i * h
        sum_fx += 2 * f(x)
    I = (h / 2) * sum_fx
    return I
# Input from user
a = float(input("Enter lower limit (a): "))
b = float(input("Enter upper limit (b): "))
n = int(input("Enter number of strips (n): "))
# Calculate
result = composite_trapezoidal(a, b, n)
print("Result using Composite Trapezoidal Rule:", result)