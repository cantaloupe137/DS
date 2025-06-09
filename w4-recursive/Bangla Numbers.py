def solve(n):
    # 'kuti' (10000000), 'lakh' (100000), 'hajar' (1000), 'shata' (100)
    result = ""
    if n >= 10000000:
        result += f'{solve(n // 10000000)} kuti '
        n = n % 10000000
    if n >= 100000:
        result += f'{solve(n // 100000)} lakh '
        n = n % 100000
    if n >= 1000:
        result += f'{solve(n // 1000)} hajar '
        n = n % 1000
    if n >= 100:
        result += f'{solve(n // 100)} shata '
        n = n % 100
    if n != 0:
        result += str(n)

    return result


count = 1
while True:
    try:
        n = int(input())
        if n == 0:
            if n == 0:
                print(f'{count:>4}. 0')
        else:
            ans = ' '.join(solve(n).split())  # 避免中間出現兩個空格
            print(f'{count:>4}. {ans}')
        count += 1
    except EOFError:
        break
