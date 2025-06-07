def solve(n, matrix):
    for i in matrix:
        # 檢查有無 < 0
        if i < 0:
            return 'Non-symmetric.'
    # 判斷是否回文
    return 'Symmetric.' if matrix == matrix[::-1] else 'Non-symmetric.'


T = int(input())
for t in range(T):
    # 如果輸入是 N = _，則取最後一項就好
    n = int(input().split()[-1])
    matrix = []
    for i in range(n):
        # 變成一維陣列
        matrix.extend(list(map(int, input().split())))

    print(f'Test #{t+1}: {solve(n, matrix)}')
