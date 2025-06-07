T = int(input())
for _ in range(T):
    n = int(input())
    source = []
    target = []
    for _ in range(n):
        source.append(input())
    for _ in range(n):
        target.append(input())

    Pt = n - 1
    Ps = n - 1

    while Ps >= 0:
        if source[Ps] == target[Pt]:
            Pt -= 1
        Ps -= 1

    while Pt >= 0:
        print(target[Pt])
        Pt -= 1

    print()