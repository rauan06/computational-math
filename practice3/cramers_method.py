import numpy as np
from typing import Union
from utils import read_matrix

def cramers_method(A: list[list[float]], b: list[float]) -> Union[list[float], str]:
    A = np.array(A, dtype=float)
    b = np.array(b, dtype=float)
    n = len(A[0])

    det_A = np.linalg.det(A)
    if abs(det_A) == 0:
        return "The determinant of matrix A is zero; the system has no unique solution."

    result = []
    for i in range(n):
        A_i = A.copy()
        A_i[:, i] = b

        det_A_i = np.linalg.det(A_i)

        result.append(round(float(det_A_i / det_A), 2))

    return result

if __name__ == '__main__':
    A, b = read_matrix()
    print(cramers_method(A, b))
