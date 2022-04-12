def searchMatrix(matrix: list[list[int]], target: int) -> bool:
    for i in range(len(matrix)):
        if (matrix[i][0] > target):
            for j in range(len(matrix[i-1])):
                if(matrix[i-1][j] == target):
                    return 'true'
            return 'false'


matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
target = 13
print(searchMatrix(matrix, target))
