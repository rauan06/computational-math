import numpy as np
from typing import Union
from utils import read_matrix

def cramers_method(A: list[list[int]], b: list[int]) -> Union[list[float], str]:
    A = np.array(A)
    b = np.array(b)
    result = []
    det_A = np.linalg.det(A)
    if det_A == 0:
        return "The determinant of matrix A is zero, the system has no unique solution."
    for i in range(len(A)):
        A_i = A.copy()
        A_i[:, i] = b
        result.append(round(float(np.linalg.det(A_i) / det_A), 2))

    return result

if __name__ == '__main__':
    A, b = read_matrix()

    print(cramers_method(A, b))