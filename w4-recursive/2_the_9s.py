def degree_9(string, a):
    total = 0
    for i in range(len(string)):
        total += int(string[i])
    a += 1
    if total == 9:
        return a
    elif total < 9:
        return -1
    else:
        return degree_9(str(total), a)


while True:
    try:
        n = input().strip()  # 有空格的話會有問題
        if n == '0':
            break
        ans = degree_9(n, 0)

        if ans == -1:
            print(f'{n} is not a multiple of 9.')
        else:
            print(f'{n} is a multiple of 9 and has 9-degree {ans}.')

    except EOFError:
        break
