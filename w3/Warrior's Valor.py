def solve(s):
    #取字串長度
    length = len(s)
    #如果字串長度<=3，直接回傳字串
    if length <= 3:
        return s
    #如果字串長度 > 3，則每多出三位增加一個數字
    lvl = (length - 1) // 3
    #取ASCII碼('A' = 65, 'a' = 97)
    character = chr(65 + lvl - 1)
    #取前3個字元，並把後面剩下的字元給輸出
    first_3_cha = s[:length % 3] if length % 3 != 0 else s[:3]
    return f'{first_3_cha}{character}'
while True:
    try:
        s = input()
        print(solve(s))
    except EOFError:
        break