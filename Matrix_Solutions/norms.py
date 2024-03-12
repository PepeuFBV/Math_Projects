import numpy as np

def calculate_euclidian_norm(matrix):
    if isinstance(matrix, np.ndarray) and matrix.ndim == 1:
        return np.sqrt(np.sum(np.square(matrix)))
    else:
        return sum(cell**2 for row in matrix for cell in row)**0.5

def calculate_max_norm(matrix):
    if isinstance(matrix, np.ndarray) and matrix.ndim == 1:
        return np.max(np.abs(matrix))
    else:
        return max(sum(abs(cell) for cell in row) for row in matrix)

def calculate_frobenius_norm(matrix):
    if isinstance(matrix, np.ndarray) and matrix.ndim == 1:
        return np.sqrt(np.sum(np.square(matrix)))
    else:
        return sum(cell**2 for row in matrix for cell in row)**0.5

def calculate_infinity_norm(matrix):
    if isinstance(matrix, np.ndarray) and matrix.ndim == 1:
        return np.max(np.abs(matrix))
    else:
        return max(sum(abs(cell) for cell in row) for row in matrix)

def calculate_row_norm(matrix):
    if isinstance(matrix, np.ndarray) and matrix.ndim == 1:
        return np.sum(np.abs(matrix))
    else:
        return [sum(abs(cell) for cell in row) for row in matrix]

def calculate_column_norm(matrix):
    if isinstance(matrix, np.ndarray) and matrix.ndim == 1:
        return np.sum(np.abs(matrix))
    else:
        return [sum(abs(matrix[i][j]) for i in range(len(matrix))) for j in range(len(matrix[0]))]