#498 - bis
def solve(x, equation):
    #計算最高的次方 e.g. [1, -1] -> n = 2 - 1 = 1
    n = len(equation) - 1
    ans = 0
    #霍納法則f(x)=(((an*x + an-1)x+an-2)x+...+a1)x + a0
    for i in range(n, 0, -1):
        ans = ans * x + i * equation[n - i]
    # 這樣寫會TLE
    # for i in range(n, 0, -1):
    #     ans = ans * x + i * equation[n - i]
    return ans
while True:
    try:
        x = int(input())
        equation = list(map(int, input().split()))
        print(solve(x, equation))
    except EOFError:
        break