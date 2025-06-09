n = int(input())
for _ in range(n):
    stack = []
    s = input()
    state = 1
    if s == '':
        print('Yes')
    else:
        for quote in s:
            if quote == '(' or quote == '[':
                stack.append(quote)
            else:
                if stack != [] and ((quote == ")" and stack[-1] == "(") or (quote == "]" and stack[-1] == "[")):
                    stack.pop()
                else:
                    state = 0
                    break
        if state == 1 and not stack:
            print("Yes")
        else:
            print("No")
