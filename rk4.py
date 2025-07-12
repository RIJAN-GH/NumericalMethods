# Rk-4 Method
def func(x, y):
    return 1 + 3 * x * x

def rk4_method(x0, y0, xn, h):
    n = round((xn - x0) / h)
    print("\n x\t\ty\t\tk1\t\tk2\t\tk3\t\tk4\t\ty_next")
    for i in range(n):
        k1 = h * func(x0, y0)
        k2 = h * func(x0 + h / 2, y0 + k1 / 2)
        k3 = h * func(x0 + h / 2, y0 + k2 / 2)
        k4 = h * func(x0 + h, y0 + k3)
        yn = y0 + (k1 + 2 * k2 + 2 * k3 + k4) / 6
        print("%.4f\t\t%.4f\t\t%.4f\t\t%.4f\t\t%.4f\t\t%.4f\t\t%.4f" % (x0, y0, k1, k2, k3, k4, yn))
        y0 = yn
        x0 = x0 + h

    print("\nAt x = %.4f, y = %.4f (approx)" % (x0, y0))

print("Enter initial guess:")
x0 = float(input("x0 = "))
y0 = float(input("y0 = "))
print("Enter value of xn:")
xn = float(input("xn = "))
print("Enter step size (h):")
h = float(input("h = "))

rk4_method(x0, y0, xn, h)