import numpy as np

def lu_method(matrix, solution): # Also known as Crout's method
    # Ax = b
    # LUx = b
    # Ly = b
    # Ux = y
    
    matrix = matrix.astype(float)
    solution = solution.astype(float)
    n = len(matrix)

    # Perform LU decomposition
    for i in range(n):
        for j in range(i+1, n):
            factor = matrix[j][i] / matrix[i][i]
            matrix[j][i] = factor
            for k in range(i+1, n):
                matrix[j][k] -= factor * matrix[i][k]
    
    # Solve Ly = b using forward substitution
    y = np.zeros(n)
    for i in range(n):
        y[i] = solution[i] - np.dot(matrix[i][:i], y[:i])

    # Solve Ux = y using back substitution
    x = np.zeros(n)
    for i in range(n-1, -1, -1):
        x[i] = (y[i] - np.dot(matrix[i][i+1:], x[i+1:])) / matrix[i][i]

    return x