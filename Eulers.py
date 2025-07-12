# Euler method 
def func(x, y):
    return 1 + 3 * x * x

def euler_method(x0, y0, xn, h):
    iter = 0
    n = round((xn - x0) / h)  # total steps
    print("\n x\t\t y\t\t m\t\t y_next")
    for i in range(n):
        m = func(x0, y0)
        yn = y0 + m * h  # Euler formula
        print("%.4f\t\t %.4f\t\t %.4f\t\t %.4f" % (x0, y0, m, yn))
        y0 = yn
        x0 = x0 + h
        iter += 1

    print("\nAt x = %.4f, y = %.4f" % (x0, y0))
    print("Total iteration:", iter)

# User input section
print("Enter initial guess:")
x0 = float(input("x0 = "))
y0 = float(input("y0 = "))
print("Enter value of xn:")
xn = float(input("xn = "))
print("Enter step size (h):")
h = float(input("h = "))
euler_method(x0, y0, xn, h)
