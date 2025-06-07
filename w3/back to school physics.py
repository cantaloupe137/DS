while True:
    try:

        v, t = map(int, input().split())
        print(2 * v * t)

    except EOFError:
        break