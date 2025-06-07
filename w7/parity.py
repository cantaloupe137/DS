def solve(n):
    return f'The parity of {n:b} is {f"{n:b}".count("1")} (mod 2).'
while True:
    try:
        n = int(input())
        if n == 0: break
        print(solve(n))
    except EOFError:
        break