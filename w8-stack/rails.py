while True:
    try:
        n = int(input())
        if n == 0:
            break

        while True:
            nums = list(map(int, input().split()))
            if nums[0] == 0:
                print()
                break

            stack = []
            idx = 0
            for i in range(1, n + 1):
                stack.append(i)
                while stack and stack[-1] == nums[idx]:
                    stack.pop()
                    idx += 1
            if not stack:
                print("Yes")
            else:
                print("No")
    except EOFError:
        break
    except ValueError:
        continue
