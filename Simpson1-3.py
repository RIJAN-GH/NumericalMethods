# Composite Simpson 1/3 Rule
def f(x):
    return 1 + x**3

# Input from user
a = float(input("Enter lower limit: "))
b = float(input("Enter upper limit: "))
n = int(input("Enter number of strips (n): "))

h = (b - a) / n
I = f(a) + f(b)
for i in range(1, n):
    if(i%2 == 0):
        I += 2*f(a + i*h)
    
    else: 
        I += 4*f(a + i*h)

print("Composite Simpson 1/3 result:", I*(h/3))