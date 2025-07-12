# Newton Backward Difference Interpolation
import numpy as np

n = int(input('Enter number of data points: '))
x = np.zeros(n)
y = np.zeros((n, n))

print('Enter data for x:')
for i in range(n):
    x[i] = float(input(f'x[{i}] = '))

print('Enter data for y:')
for i in range(n):
    y[i][0] = float(input(f'y[{i}] = '))

for i in range(1, n):
    for j in range(n-1, i-1, -1):
        y[j][i] = y[j][i-1] - y[j-1][i-1]

print('\nBACKWARD DIFFERENCE TABLE:')
for i in range(n):
    print(f'{x[i]:.2f}', end='')
    for j in range(i + 1):
        print(f'\t{y[i][j]:.2f}', end='')
    print()
