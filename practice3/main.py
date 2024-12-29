from utils import read_matrix
from cramers_method import cramers_method
from gaussian_method import gaussian_method
from jacobi_method import jacobi_method
from seidel_gauss_method import seidel_gauss_method

def main():
    # Read the matrix and vector from the file
    A, b = read_matrix()

    # Apply Cramer's method
    cramers_result = cramers_method(A, b)
    print("Cramer's Method Result:", cramers_result)

    # Apply Gaussian method
    gaussian_result = gaussian_method(A, b)
    print("Gaussian Method Result:", gaussian_result)

    # Apply Jacobi method
    jacobi_result = jacobi_method(A, b)
    print("Jacobi Method Result:", jacobi_result)

    # Apply Seidel-Gauss method
    seidel_gauss_result = seidel_gauss_method(A, b)
    print("Seidel-Gauss Method Result:", seidel_gauss_result)

if __name__ == '__main__':
    main()