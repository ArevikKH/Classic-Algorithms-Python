import numpy as np

def gaussian_elimination(A, b):
    n = len(b)

    for pivot_row in range(n):
        for row in range(pivot_row + 1, n):
            factor = A[row, pivot_row] / A[pivot_row, pivot_row]
            A[row, pivot_row:] -= factor * A[pivot_row, pivot_row:]
            b[row] -= factor * b[pivot_row]

    x = np.zeros(n)
    for row in range(n - 1, -1, -1):
        x[row] = (b[row] - np.dot(A[row, row + 1:], x[row + 1:])) / A[row, row]

    return x

A = np.array([[1.0, 3.0, 2.0],
              [2.0, 7.0, 5.0],
              [1.0, 4.0, 6.0]])
b = np.array([1.0, 18.0, 26.0])
print(gaussian_elimination(A, b))
