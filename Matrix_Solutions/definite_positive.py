import numpy as np

def is_definite_positive(matrix):
    matrix = matrix.astype(float)
    n = len(matrix)
    for i in range(n):
        for j in range(i):
            matrix[i][i] -= matrix[i][j] ** 2
        matrix_copy = matrix.copy()
        eigenvalues = np.linalg.eigvals(matrix_copy)
        if np.all(eigenvalues > 0):
            return True
        else:
            return False