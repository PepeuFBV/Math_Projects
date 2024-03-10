import numpy as np
import sys
sys.path.append('..')
from definite_positive import is_definite_positive as is_df

def llt_method(matrix, solution): # Also known as Cholesky decomposition
    # Ax = b
    # LLtx = b
    # Ly = b
    # Ltx = y
    
    matrix = matrix.astype(float)
    solution = solution.astype(float)
    n = len(matrix)

    if not is_df(matrix):
        return "The matrix is not definite positive, impossible to solve using LLt method."

    # Perform LLt decomposition
    for i in range(n):
        for j in range(i):
            matrix[i][i] -= matrix[i][j] ** 2
        if matrix[i][i] <= 0:
            raise ValueError("Matrix is not definite positive")
        matrix[i][i] = np.sqrt(matrix[i][i])
        for j in range(i+1, n):
            for k in range(i):
                matrix[j][i] -= matrix[j][k] * matrix[i][k]
            if matrix[i][i] == 0:
                raise ValueError("Zero pivot encountered")
            matrix[j][i] /= matrix[i][i]
    
    # Solve Ly = b using forward substitution
    y = np.zeros(n)
    for i in range(n):
        y[i] = solution[i] - np.dot(matrix[i][:i], y[:i])

    # Solve Ltx = y using back substitution
    x = np.zeros(n)
    for i in range(n-1, -1, -1):
        if matrix[i][i] == 0:
            raise ValueError("Zero pivot encountered")
        x[i] = (y[i] - np.dot(matrix[i][i+1:], x[i+1:])) / matrix[i][i]

    return x