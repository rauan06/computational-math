from typing import Tuple

def read_matrix() -> Tuple[list[list[int]], list[int]]:
    n = int(input().strip())
    A, b = [], []

    for i in range(n):
        equation = list(map(int, input().strip().split()))
        A.append(equation[:-1])
        b.append(equation[-1])
    
    return A, b