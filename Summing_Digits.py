def solve(n):
    while n >= 10:
        n = sum(map(int, str(n)))
    return n

while True:
    n = int(input())
    if n == 0:
        break
    print(solve(n))