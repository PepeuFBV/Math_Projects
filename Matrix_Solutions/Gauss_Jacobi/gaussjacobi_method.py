import numpy as np
import sys
sys.path.append('../')
from dominant_diagonal import is_dominant_diagonal as is_dd

def gauss_jacobi_method(matrix, solution, max_iterations, norm_func, tolerance):
    if not is_dd(matrix):
        return "The matrix is not diagonally dominant, impossible to solve using the Gauss-Jacobi method."
    
    matrix = matrix.astype(float)
    solution = solution.astype(float)
    n = len(matrix)
    x = np.zeros(n)
    D = np.zeros((n, n))
    L = np.zeros((n, n))
    U = np.zeros((n, n))
    
    for i in range(n):
        D[i][i] = matrix[i][i]
        for j in range(n):
            if i > j:
                L[i][j] = matrix[i][j]
            elif i < j:
                U[i][j] = matrix[i][j]
    
    iterations = 0
    while iterations < max_iterations:
        x_old = x.copy()
        x = np.dot(np.linalg.inv(D), solution - np.dot((L + U), x))
        if norm_func(x - x_old) < tolerance:
            break
        iterations += 1

    return x, iterations