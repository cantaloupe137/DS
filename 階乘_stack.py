MOD = 10**9 + 7
MAX_N = 1000

factorials = [1] * (MAX_N + 1)
for i in range(1, MAX_N + 1):
    factorials[i] = (factorials[i - 1] * i) % MOD

try:
    while True:
        line = input()
        if line.strip() == "":
            continue
        n = int(line.strip())
        print(factorials[n])
except EOFError:
    pass
