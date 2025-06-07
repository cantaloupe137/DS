"""
公式:
𝑆(𝑛, 𝑚) = 𝑚𝑆(𝑛 − 1, 𝑚) + 𝑆(𝑛 − 1, 𝑚 − 1), for integers 1 < 𝑚 < 𝑛.
"""
def S(n, m):
    if m == n or m == 1:
        return 1
    if m == 0 or m > n:
        return 0
    return m % 2 * S(n - 1, m) + S(n - 1, m - 1) % 2
t = int(input())
#處理輸入可能是空行的問題
while True:
    line = input().strip()
    if line:
        break

for _ in range(t):
    n, m = map(int, line.split())
    print(S(n, m))