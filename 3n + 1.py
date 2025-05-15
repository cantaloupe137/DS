# the 3n + 1 problem
"""
1. input n
2. print n
3. if n = 1 then STOP
4. if n is odd then n ←− 3n + 1
5. else n ←− n/2
6. GOTO 2
"""
# 建立一個字典，儲存計算次數
dict_a = {}
# 計算循環次數，直到數字等於1


def solve(n):
    # 如果n存在字典裡的話，直接return
    if n in dict_a:
        return dict_a[n]
    # 如果n等於1，return 1
    if n == 1:
        return 1
    # n 是奇數， m <- 3n + 1
    if n % 2 != 0:
        m = 3 * n + 1
    # n 若是偶數，則 n 除以 2
    else:
        m = n // 2
    dict_a[n] = solve(m) + 1
    return dict_a[n]


while True:
    try:
        # 輸入x, y
        x, y = map(int, input().split())
    except EOFError:
        break
    # 最大循環次數
    max_cycle = 0
    # 從x和y兩數循環，要從小排到大
    for i in range(min(x, y), max(x, y) + 1):
        n = solve(i)

        if n > max_cycle:
            max_cycle = n
    print(x, y, max_cycle)
