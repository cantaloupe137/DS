def solve(n, codes):
    dream = []
    for code in codes:
        if code[0] == 'Sleep':
            dream.append(code[1])
        elif code[0] == 'Test':
            if dream:
                print(dream[-1])
            else:
                print('Not in a dream')
        elif code[0] == 'Kick':
            if dream:
                dream.pop()
n = int(input())
while True:
    try:
        codes = []
        for i in range(n):
            codes.append(input().split())
        solve(n, codes)
    except EOFError:
        break