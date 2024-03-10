import numpy as np
import sys
sys.path.append('../')
from dominant_diagonal import is_dominant_diagonal as is_dd

def gauss_seidel_method(matrix, solution, iterations):
    if not is_dd(matrix):
        return "The matrix is not diagonally dominant, impossible to solve using Gauss-Seidel method."
    
    # Ax = b
    # (D+L)x = b - Ux
    # x = inv(D+L)(b - Ux)
    
    n = len(matrix)
    x = np.zeros(n)
    
    for i in range(iterations):
        for j in range(n):
            temp = solution[j]
            for k in range(n):
                if j != k:
                    temp -= matrix[j][k] * x[k]
            x[j] = temp / matrix[j][j]
    return x