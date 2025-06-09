"""
you can say 11 此題要求的是11的倍數
不是0的話 -> 繼續輸入
11的倍數判斷方法: 奇位數和偶位數的差為11的倍數
即為減完的11取餘數是否 = 0
"""

while True:
    n = input().strip()
    if n == '0':
        break
    even_i = n[0::2]
    even_sum = sum(map(int, even_i))

    odd_i = n[1::2]
    odd_sum = sum(map(int, odd_i))

    check = True
    if abs(odd_sum - even_sum) % 11 == 0:
        print(f'{n} is a multiple of 11.')
    else:
        print(f'{n} is not a multiple of 11.')