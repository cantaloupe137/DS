while True:
    try:
        n = int(input())
        print(int(n * 1.5))
    except EOFError:
        break
