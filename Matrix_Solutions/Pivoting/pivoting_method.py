import numpy as np

def pivoting_method(matrix, solution):
    matrix = matrix.astype(float)
    solution = solution.astype(float)
    n = len(matrix)

    for i in range(n):
        # Find the row with the largest absolute value in column i
        max_row = i
        for j in range(i+1, n):
            if abs(matrix[j][i]) > abs(matrix[max_row][i]):
                max_row = j

        # Swap the rows
        matrix[[i, max_row]] = matrix[[max_row, i]]
        solution[[i, max_row]] = solution[[max_row, i]]

        # Perform elementary row operations to eliminate the values below the pivot
        for j in range(i+1, n):
            factor = matrix[j][i] / matrix[i][i]
            matrix[j] -= factor * matrix[i]
            solution[j] -= factor * solution[i]

    # Back substitution to find the solution vector x
    x = np.zeros(n)
    for i in range(n-1, -1, -1):
        x[i] = (solution[i] - np.dot(matrix[i][i+1:], x[i+1:])) / matrix[i][i]

    return x