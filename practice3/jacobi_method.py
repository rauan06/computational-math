from typing import List, Union
from utils import read_matrix

def jacobi_method(A: List[List[float]], b: List[float], max_iterations: int = 100, tolerance: float = 1e-10) -> Union[List[float], str]:
    n = len(A)
    x = [0.0] * n
    x_new = x[:]

    for iteration in range(max_iterations):
        for i in range(n):
            if A[i][i] == 0:
                return "Division by zero detected in matrix diagonal."

            s = sum(A[i][j] * x[j] for j in range(n) if j != i)
            x_new[i] = (b[i] - s) / A[i][i]

        # Check for convergence
        if max(abs(x_new[i] - x[i]) for i in range(n)) < tolerance:
            return x_new

        x = x_new[:]

    return x

if __name__ == '__main__':
    A, b = read_matrix()
    print(jacobi_method(A, b))
