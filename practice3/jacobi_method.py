from typing import List, Union
from utils import read_matrix

def jacobi_method(A: List[List[float]], b: List[float]) -> Union[List[float], str]:
    pass

if __name__ == '__main__':
    A, b = read_matrix()
    print(jacobi_method(A, b))
