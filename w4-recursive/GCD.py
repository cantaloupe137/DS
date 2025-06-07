def GCD(a, b):
    if b == 0:
        return a
    return GCD(b, a % b)

def G(n):
    G = 0
    for i in range(1, n):
        for j in range(i + 1, n + 1):
            G += GCD(i, j)
    return G

while True:
    n = int(input())
    if n == 0:
        break
    print(G(n))
