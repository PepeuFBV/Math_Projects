import numpy as np
import sys
sys.path.append('../')
from dominant_diagonal import is_dominant_diagonal as is_dd

def gauss_seidel_method(matrix, solution, max_iterations, norm_func, tolerance):
    if not is_dd(matrix):
        return "The matrix is not diagonally dominant, impossible to solve using Gauss-Seidel method."
    
    n = len(matrix)
    x = np.zeros(n)
    iterations = 0
    
    for _ in range(max_iterations):
        x_old = np.copy(x)
        for i in range(n):
            temp = solution[i]
            for j in range(n):
                if i != j:
                    temp -= matrix[i][j] * x[j]
            x[i] = temp / matrix[i][i]
        
        iterations += 1
        # Check convergence
        if norm_func(x - x_old) < tolerance:
            return x, iterations
    
    return x, iterations