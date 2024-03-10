import numpy as np

def is_dominant_diagonal(matrix):
    n = len(matrix)
    for i in range(n):
        temp = 0
        for j in range(n):
            if i != j:
                temp += abs(matrix[i][j])
        if abs(matrix[i][i]) < temp:
            return False
    return True