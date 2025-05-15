def solve(n1, n2):
    # 用dict存n1和n2的每個字母出現的次數
    ans = ('')
    n1Dict, n2Dict = {}, {}
    for i in n1:
        # 因為default預設 'none'，如果default + 1會有type error，所以要變成0
        n1Dict[i] = n1Dict.get(i, 0) + 1
    for i in n2:
        n2Dict[i] = n2Dict.get(i, 0) + 1
    for key, item in n1Dict.items():
        if key in n1 and key in n2:
            # 取出現過的字元
            ans += f'{key}' * min(n1Dict[key], n2Dict[key])
    return ''.join(sorted(ans))


while True:
    try:
        n1 = input()
        n2 = input()
        print(solve(n1, n2))
    except EOFError:
        break
    except ValueError:
        continue
