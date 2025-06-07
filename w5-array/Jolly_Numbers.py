def solve(n, lst):
    # 把數列兩兩之間的公差由小排到大
    jolly = sorted([abs(lst[i] - lst[i - 1]) for i in range(1, n)])
    for i in range(1, n):
        # 檢查第i項的值是否等於i
        if jolly[i - 1] != i:
            return 'Not jolly'
    return 'Jolly'


while True:
    try:
        lst = list(map(int, input().split()))
        n = lst[0]
        # 第一項是n，所以要從第二項開始
        print(solve(n, lst[1:]))
    except EOFError:
        break
    except ValueError:
        continue
