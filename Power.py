# Matrix A and initial parameters for power method
import numpy as np

# Define matrix A
A = np.array([
    [1, 2, 0],
    [2, 1, 0],
    [0, 0, -1]
], dtype=float)

# Initial guess vector X
X = np.array([1, 1, 1], dtype=float)

# Tolerable error
error = 0.0001

# Power Method Implementation
lambda_old = 1.0
iteration_data = []

while True:
    # Multiply A with X to get new vector
    X_new = A @ X

    # Find the largest absolute value (dominant eigenvalue estimate)
    lambda_new = max(abs(X_new))

    # Normalize the new vector
    X = X_new / lambda_new

    # Store iteration data for inspection
    iteration_data.append((lambda_new, X.copy()))

    # Check for convergence
    if abs(lambda_new - lambda_old) <= error:
        break

    lambda_old = lambda_new

# Output final result
lambda_new, X_final = lambda_new, X
lambda_new, X_final.round(4).tolist(), iteration_data[-5:]  # Show last 5 iterations for context
