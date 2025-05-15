def solve(sums, different):
    # sum : 分數之和, different : 分數之差
    # 如果相差的數字大於總和，則return 'impossible'
    if different > sums:
        return 'impossible'
    y = (sums - different) / 2
    x = (sums + different) / 2
    # 檢查y是不是整數
    # 如果y不是整數，則return 'impossible'
    if not (y == int(y)):
        return 'impossible'
    return f'{int(x)} {int(y)}'


T = int(input())
for t in range(T):
    sums, different = list(map(int, input().split()))
    print(solve(sums, different))
