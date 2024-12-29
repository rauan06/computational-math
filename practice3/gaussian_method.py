def gaussian_method4x4(A : list[int], b : list[int]) -> list[int]:
    for i in range(4):
        for j in range(i + 1, 4):
            ratio = A[j][i] / A[i][i]
            for k in range(4):
                A[j][k] -= ratio * A[i][k]
            b[j] -= ratio * b[i]

    x = [0] * 4
    for i in range(3, -1, -1):
        x[i] = b[i]
        for j in range(i + 1, 4):
            x[i] -= A[i][j] * x[j]
        x[i] /= A[i][i]

    return x

if __name__ == '__main__':
    n = int(input().strip())
    A, b = [], []

    for i in range(n):
        equation = list(map(int, input().strip().split()))
        A.append(equation[:4])
        b.append(equation[4])

    print(gaussian_method4x4(A, b))