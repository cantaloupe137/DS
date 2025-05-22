def solve(n, codes):
    dream = []  # 放答案
    for code in codes:  # codes放所有的指令，code每行的指令
        if code[0] == 'Sleep':  # 進入夢境
            dream.append(code[1])
        # 如果在夢境裡，print出在夢境的最後一個人
        # 不在的話，print 'Not in a dream'
        elif code[0] == 'Test':
            if dream:
                print(dream[-1])
            else:
                print('Not in a dream')
        # Kick的話，把夢境的最後一個給pop掉
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
