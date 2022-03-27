from xmlrpc.client import boolean
from Matrix_Input import matrixInput


def matrixMultiplication(m: int, n: int, A: list, B: list) -> list:
    result = []
    for i in range(m):
        row = []
        for j in range(n):
            cell = 0
            for k in range(m):
                cell += (A[i][k] * B[k][j])
            row.append(cell)
        result.append(row)
    return result


def validate(m1, n1, m2, n2) -> boolean:
    if ((m1 == n2) or (n1 == m2)):
        return True
    else:
        return False


if __name__ == '__main__':
    m, n = map(int, input("rows x columns: ").split('x'))

    print('Enter the values of matrix 1:')
    A = matrixInput(m, n)

    print('Enter the values of matrix 2:')
    B = matrixInput(m, n)
    print(f"matrix A: {A}")
    print(f"matrix B: {B}")

    print(matrixMultiplication(m, n, A, B))

'''
2x2
1
2
3
4
5
6
7
8
'''
