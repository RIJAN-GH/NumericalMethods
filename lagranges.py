# Lagrange's Interpolation
import numpy as np

n = int(input("Enter number of data points: "))
x = np.zeros(n)
y = np.zeros(n)

print(f'Enter {n} data points for x:')
for i in range(n):
    x[i] = float(input(f'x[{i}] = '))

print(f'Enter {n} data points for y:')
for i in range(n):
    y[i] = float(input(f'y[{i}] = '))

xp = float(input('Enter interpolation point: '))
yp = 0

for i in range(n):
    p = 1
    for j in range(n):
        if i != j:
            p *= (xp - x[j]) / (x[i] - x[j])
    yp += p * y[i]

print('Interpolated value at %.3f is %.3f.' % (xp, yp))
