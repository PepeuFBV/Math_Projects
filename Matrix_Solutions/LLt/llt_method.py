import numpy as np

def llt_method(matrix, solution): # Also known as Cholesky decomposition
    # Ax = b
    # LLtx = b
    # Ly = b
    # Ltx = y
    
    matrix = matrix.astype(float)
    solution = solution.astype(float)
    n = len(matrix)

    # Perform LLt decomposition
    for i in range(n):
        for j in range(i):
            matrix[i][i] -= matrix[i][j] ** 2
        matrix[i][i] = np.sqrt(matrix[i][i])
        for j in range(i+1, n):
            for k in range(i):
                matrix[j][i] -= matrix[j][k] * matrix[i][k]
            matrix[j][i] /= matrix[i][i]
    
    # Solve Ly = b using forward substitution
    y = np.zeros(n)
    for i in range(n):
        y[i] = solution[i] - np.dot(matrix[i][:i], y[:i])

    # Solve Ltx = y using back substitution
    x = np.zeros(n)
    for i in range(n-1, -1, -1):
        x[i] = (y[i] - np.dot(matrix[i][i+1:], x[i+1:])) / matrix[i][i]

    return x