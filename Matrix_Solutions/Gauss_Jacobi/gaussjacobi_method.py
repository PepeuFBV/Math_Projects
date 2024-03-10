import numpy as np
import sys
sys.path.append('../')
from dominant_diagonal import is_dominant_diagonal as is_dd

# TODO: Add support for stopping before the maximum number of iterations, with a "tolerance" parameter

def gauss_jacobi_method(matrix, solution, max_iterations):
    if not is_dd(matrix):
        return "The matrix is not diagonally dominant, impossible to solve using the Gauss-Jacobi method."
    
    # Ax = b
    # Dx = b - (L+U)x
    # x = inv(D)(b - (L+U)x)
    
    matrix = matrix.astype(float)
    solution = solution.astype(float)
    n = len(matrix)
    x = np.zeros(n)
    D = np.zeros((n, n))
    L = np.zeros((n, n))
    U = np.zeros((n, n))
    
    # Splitting the matrix into D, L, and U
    for i in range(n):
        D[i][i] = matrix[i][i]
        for j in range(n):
            if i > j:
                L[i][j] = matrix[i][j]
            elif i < j:
                U[i][j] = matrix[i][j]
    
    # Performing the iterations
    for _ in range(max_iterations):
        x = np.dot(np.linalg.inv(D), solution - np.dot((L + U), x))
    
    return x