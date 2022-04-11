from Matrix_Input import matrixInput, mCompatibility


def matrixMultiplication(m1: int, n1: int, m2: int, n2: int, A: list, B: list) -> list:
    result = []
    for i in range(m1):
        row = []
        for j in range(n2):
            cell = 0
            for k in range(n1):
                cell += (A[i][k] * B[k][j])
            row.append(cell)
        result.append(row)
    return result


if __name__ == '__main__':
    m1, n1 = map(int, input("For matrix1, rows x columns: ").split('x'))
    m2, n2 = map(int, input("For matrix2, rows x columns: ").split('x'))

    print('Enter the values of matrix 1:')
    A = matrixInput(m1, n1)

    print('Enter the values of matrix 2:')
    B = matrixInput(m2, n2)

    m1, n1, m2, n2, A, B, compatible = mCompatibility(m1, n1, m2, n2, A, B)
    if compatible:
        print(matrixMultiplication(m1, n1, m2, n2, A, B))
    else:
        print(-1)
