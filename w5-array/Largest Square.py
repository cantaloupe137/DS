def check(m, n, row, col):
    mid = matrix[row][col]
    length = 1
    index = 1
    while True:
        newLength = length + 2
        topLeftRow, topLeftCol = row - index, col - index

        if not (0 <= topLeftRow < m and 0 <= topLeftCol < n and
                topLeftRow + newLength - 1 < m and topLeftCol + newLength - 1 < n):
            return length

        for i in range(newLength):
            if not (matrix[topLeftRow][topLeftCol + i] == mid and
                    matrix[topLeftRow + newLength - 1][topLeftCol + i] == mid and
                    matrix[topLeftRow + i][topLeftCol] == mid and
                    matrix[topLeftRow + i][topLeftCol + newLength - 1] == mid):
                return length

        length = newLength
        index += 1


T = int(input())
for t in range(T):
    m, n, q = list(map(int, input().split()))
    matrix = []
    for i in range(m):
        matrix.append(list(input()))

    centers = []
    for i in range(q):
        centers.append(list(map(int, input().split())))

    print(f'{m} {n} {q}')
    for row, col in centers:
        print(check(m, n, row, col))