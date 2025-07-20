# Composite Simpson 3/8 Rule
def f(x):
    return 1 + x**3

# Input from user
a = float(input("Enter lower limit: "))
b = float(input("Enter upper limit: "))
n = int(input("Enter number of strips (n): "))

h = (b - a) / n
I = f(a) + f(b) + 3*f(a+h)
for i in range(1, n):
    if(i%3 == 0):
        I += 2*f(a + i*h)

    elif(i%2 == 0): 
        I += 3*f(a + i*h)
    
    else:
        continue

print("Composite Simpson 3/8 result:", I*(3*h/8))