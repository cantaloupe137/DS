n = int(input())
for i in range(1, n + 1):
    # 輸入上界和下界
    down = int(input())
    up = int(input())
    # 如果下界是偶數，就+1
    if down % 2 == 0:
        down += 1
    # 如果上界是偶數，就-1
    if up % 2 == 0:
        up -= 1
    # 計算有幾個奇數
    n = (up - down) / 2 + 1
    # 輸出奇數的和
    # 等差級數公式: Sn = n/2 * (首項 + 末項)
    print(f'Case {i}: {int(n * (up + down) / 2)}')
