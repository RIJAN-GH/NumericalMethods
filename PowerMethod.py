# Step 2: Input
n = int(input("Enter the order of the matrix (n): "))
error = float(input("Enter the tolerable error (e): "))

# Step 3: Read matrix A
a = [[0.0 for _ in range(n)] for _ in range(n)]
print("Enter the matrix elements row by row:")
for i in range(n):
    for j in range(n):
        a[i][j] = float(input(f"A[{i}][{j}]: "))

# Step 4: Read initial guess vector X
x = [0.0 for _ in range(n)]
print("Enter initial guess vector X:")
for i in range(n):
    x[i] = float(input(f"X[{i}]: "))

# Step 5: Initialize
lambda_old = 1.0

while True:
    # Step 6: Multiplication X_NEW = A * X
    x_new = [0.0 for _ in range(n)]
    for i in range(n):
        for j in range(n):
            x_new[i] += a[i][j] * x[j]

    # Step 7: Replace X by X_NEW
    x = x_new[:]

    # Step 8: Finding Largest (Lambda_New)
    lambda_new = abs(x[0])
    for i in range(1, n):
        if abs(x[i]) > lambda_new:
            lambda_new = abs(x[i])

    # Step 9: Normalization
    for i in range(n):
        x[i] = x[i] / lambda_new

    # Step 10: Display
    print(f"\nApproximate Eigenvalue: {lambda_new}")
    print("Corresponding Eigenvector:")
    for val in x:
        print(round(val, 4), end=' ')
    print()

    # Step 11: Checking Accuracy
    if abs(lambda_new - lambda_old) <= error:
        break
    lambda_old = lambda_new