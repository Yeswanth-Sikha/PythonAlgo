def matrixInput(m, n):
    matrix = []
    for i in range(m):
        temp = []
        for j in range(n):
            value = int(input(f"{i},{j}: "))
            temp.append(value)
        matrix.append(temp)
    return matrix


if __name__ == '__main__':
    m, n = map(int, input("rows x columns: ").split('x'))
    A, B = [], []
    print('Enter the values of matrix 1:')
    A = matrixInput(m, n)
    print('Enter the values of matrix 2:')
    B = matrixInput(m, n)

    print(f"matrix 1: {A}")
    print(f"matrix 2: {B}")
