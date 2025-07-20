def gauss_elimination(A, n):
    # Forward Elimination
    for i in range(n):
        if A[i][i] == 0:
            print("Mathematical Error!")
            return None

        for j in range(i + 1, n):
            ratio = A[j][i] / A[i][i]
            for k in range(n + 1):
                A[j][k] = A[j][k] - ratio * A[i][k]

    # Back Substitution
    X = [0 for _ in range(n)]
    X[n - 1] = A[n - 1][n] / A[n - 1][n - 1]

    for i in range(n - 2, -1, -1):
        X[i] = A[i][n]
        for j in range(i + 1, n):
            X[i] -= A[i][j] * X[j]
        X[i] = X[i] / A[i][i]


    print("Solutions:")
    for i in range(n):
        print(f"X{i + 1} = {X[i]:.4f}")

A = [
    [1, 2, 3, 6],
    [2, 3, 5, 10],
    [2, -1, 3, 4]
]
n = 3

gauss_elimination(A, n)

