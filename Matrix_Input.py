def matrixInput(m, n):
    matrix = []
    for i in range(m):
        temp = []
        for j in range(n):
            value = int(input(f"{i},{j}: "))
            temp.append(value)
        matrix.append(temp)
    return matrix


def mCompatibility(m1, n1, m2, n2, A, B):
    if (n1 == m2):
        return m1, n1, m2, n2, A, B, True
    elif (m1 == n2):
        return m2, n2, m1, n1, B, A, True
    else:
        return m1, n1, m2, n2, A, B, False


if __name__ == '__main__':
    m1, n1 = map(int, input("For matrix1: rows x columns: ").split('x'))
    m2, n2 = map(int, input("For matrix2: rows x columns: ").split('x'))
    A, B = [], []
    print('Enter the values of matrix 1:')
    A = matrixInput(m1, n1)
    print('Enter the values of matrix 2:')
    B = matrixInput(m2, n2)

    m1, n1, m2, n2, A, B = mCompatibility(m1, n1, m2, n2, A, B)

    print(f"matrix 1: {A}")
    print(f"matrix 2: {B}")
