# train shuffle
from collections import deque


def solve(n, origin, re):

    re = deque(re)
    temp = []
    for i in origin:
        while temp and re and temp[-1] == re[0]:
            temp.pop()
            re.popleft()
        if re and i == re[0]:
            re.popleft()
        else:
            temp.append(i)
    while temp and re:
        if temp[-1] == re[0]:
            temp.pop()
            re.popleft()
        else:
            return "Fail"
    return "Success" if not re else "Fail"


try:
    while True:
        n = int(input())
        origin = list(map(int, input().split()))
        re = list(map(int, input().split()))
        print(solve(n, origin, re))
except EOFError:
    pass
