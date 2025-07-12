def f(x):
    return x**2-4*x-10
x1 = float(input("Enter the value of x1: "))
x2 = float(input("Enter the value of x2: "))
E = float(input("Enter the stoping creterion E: "))
for k in range(1,20):
    x0 = (x1 + x2) / 2
    if abs(f(x0)) < E:
        print("The root is:", x0)
        break
    else:
        if (f(x0) * f(x1)) < 0:
            x2 = x0
        else:
            x1 = x0
        print("Iteration", k, "x0 =", x0)
else:
    print("The method did not converge within 20 iterations.")
    print("Last x0 =", x0)

