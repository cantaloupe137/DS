MOD = 10 ** 9 + 7

def fac(n):
    if n:
        return n * fac(n - 1) % MOD
    return 1


while True:
    try:
        n = int(input())
        print(fac(n))
    except EOFError:
        break
