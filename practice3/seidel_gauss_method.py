from typing import List, Union
from utils import read_matrix

def seidel_gauss_method(A: List[List[float]], b: List[float], max_iterations: int = 100, tolerance: float = 1e-10) -> Union[List[float], str]:
    n = len(A)
    x = [0.0] * n

    for iteration in range(max_iterations):
        x_new = x[:]
        for i in range(n):
            if A[i][i] == 0:
                return "Division by zero detected in matrix diagonal."

            s1 = sum(A[i][j] * x_new[j] for j in range(i))
            s2 = sum(A[i][j] * x[j] for j in range(i + 1, n))
            x_new[i] = (b[i] - s1 - s2) / A[i][i]

        if max(abs(x_new[i] - x[i]) for i in range(n)) < tolerance:
            return x_new

        x = x_new[:]

    return x

if __name__ == '__main__':
    A, b = read_matrix()
    print(seidel_gauss_method(A, b))