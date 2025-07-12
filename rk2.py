def func(x, y):
    # Define the differential equation dy/dx = f(x, y)
    return 1 + 3 * x * x 

def rk2_method(x0, y0, xn, h):
    n = round((xn - x0) / h)
    print("\n x\t\t y\t\t k1\t\t k2\t\t y_next")
    for i in range(n):
        k1 = func(x0, y0)
        k2 = func(x0 + h, y0 + h * k1)
        yn = y0 + (h / 2) * (k1 + k2)
        print("%.4f\t\t %.4f\t\t %.4f\t\t %.4f\t\t %.4f" % (x0, y0, k1, k2, yn))
        y0 = yn
        x0 = x0 + h

    print("\nAt x = %.4f, y = %.4f (approx)" % (x0, y0))

# Taking inputs from user
print("Enter initial guess:")
x0 = float(input("x0 = "))
y0 = float(input("y0 = "))
print("Enter value of xn:")
xn = float(input("xn = "))
print("Enter step size (h):")
h = float(input("h = "))

rk2_method(x0, y0, xn, h)
