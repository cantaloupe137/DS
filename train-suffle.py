def solve(n, origin, re):
    queue = []
    for i in origin:
        if re and re[0] == i:
            re.pop(0)
        elif re and re[-1] == i:
            re.pop()
        else:
            return "Fail"
    return "Success" if not re else "Fail"


while True:
    try:
        res = []
        n = int(input())
        origin = list(map(int, input().split()))
        re = list(map(int, input().split()))
        res.append(solve(n, origin, re))
        for result in res:
            print(result)
    except EOFError:
        break
