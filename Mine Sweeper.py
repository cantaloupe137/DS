def solve(row, col, field):
    check = [
        (-1, -1), # 上 左
        (-1, 0), # 上
        (-1, 1), # 上 右

        (0, -1), # 左
        (0, 1), # 右

        (1, -1), # 下 左
        (1, 0), # 下
        (1, 1), # 下 右
    ]
    ans = [[0 for c in range(col)] for r in range(row)]
    for r in range(row):
        for c in range(col):
            if field[r][c] == '*':
                ans[r][c] = '*'
                continue
            count = 0
            for checks in check:
                if 0 <= r + checks[0] < row and 0 <= c + checks[1] < col:
                    if field[r + checks[0]][c + checks[1]] == '*':
                        count += 1
            ans[r][c] = str(count)
    return '\n'.join([''.join(i) for i in ans])
t = 1
while True:
    try:
        row, col = list(map(int, input().split()))
        if row == 0 and col == 0:
            break
        field = []
        for i in range(row):
            field.append(list(input()))
        if t != 1: print()
        print(f'Field #{t}:\n{solve(row, col, field)}')
        t += 1
    except EOFError:
        break
