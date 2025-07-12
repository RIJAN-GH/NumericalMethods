# from math import tan, e
# def f(x):
#     return x*tan(x) - 1
# x1 = float(input("Enter the value of x1: "))
# x2 = float(input("Enter the value of x2: "))
# E = float(input("Enter the stoping creterion E: "))
# for k in range(1,20):
#     x0 = x1 + (x2 - x1) / (f(x1) - f(x2)) * f(x1)
#     if abs(f(x0)) < E:
#         print("The root is:", x0)
#         break
#     else:
#         if (f(x0) * f(x1)) < 0:
#             x2 = x0
#         else:
#             x1 = x0
#         print("Iteration", k, "x0 =", x0)
# else:
#     print("The method did not converge within 20 iterations.")
#     print("Last x0 =", x0)

from math import tan, e

def f(x):
    return x*tan(x) - 1

x1 = float(input("Enter the value of x1: "))
x2 = float(input("Enter the value of x2: "))
E = float(input("Enter the stopping criterion E: "))

print(f"{'Iter':^5} {'x1':^10} {'x2':^10} {'x0':^12} {'f(x0)':^12} {'|f(x0)|':^10}")

for k in range(1, 21):
    x0 = x1 + (x2 - x1) / (f(x1) - f(x2)) * f(x1)
    fx0 = f(x0)
    print(f"{k:^5} {x1:^10.6f} {x2:^10.6f} {x0:^12.6f} {fx0:^12.6f} {abs(fx0):^10.6f}")

    if abs(fx0) < E:
        print(f"\n✅ Root found at x = {x0:.6f} in {k} iterations.")
        break
    elif f(x1) * fx0 < 0:
        x2 = x0
    else:
        x1 = x0
else:
    print("\n⚠️ Method did not converge within 20 iterations.")
    print(f"Last x0 = {x0:.6f}")