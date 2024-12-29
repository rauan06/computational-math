import numpy as np
from typing import Union
from utils import read_matrix

def gaussian_method(A: list[list[float]], b: list[float]) -> Union[list[float], str]:
    A = np.array(A, dtype=float)
    b = np.array(b, dtype=float)
    n = len(A)

    for i in range(n):
        max_row = max(range(i, n), key=lambda r: abs(A[r][i]))
        if A[max_row][i] == 0:
            return "No unique solution exists"

        if max_row != i:
            A[[i, max_row]] = A[[max_row, i]]
            b[i], b[max_row] = b[max_row], b[i]

        for j in range(i + 1, n):
            ratio = A[j][i] / A[i][i]
            A[j, i:] -= ratio * A[i, i:]
            b[j] -= ratio * b[i]

    x = [0] * n
    for i in range(n - 1, -1, -1):
        x[i] = (b[i] - sum(A[i][j] * x[j] for j in range(i + 1, n))) / A[i][i]

    return [round(float(sol), 2) for sol in x]

if __name__ == '__main__':
    A, b = read_matrix()
    print(gaussian_method(A, b))
