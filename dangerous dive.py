while True:
    try:
        m, n = map(int, input().split())
        lst = list(map(int, input().split()))
    except EOFError:
        break

    if m == n:
        print("*")
    else:
        for i in range(1, m+1):
            if i not in lst:
                print("{} ".format(i), end="")
        print("")
