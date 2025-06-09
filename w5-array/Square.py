def dfs(length, finish, add, start, used, sticks, n):

    if finish == 3:  # 已完成3條邊，第4條邊自動完成
        return True

    if add == length:  # 當前邊已完成，開始下一條邊
        return dfs(length, finish + 1, 0, 0, used, sticks, n)

    for i in range(start, n):
        if not used[i] and add + sticks[i] <= length:
            used[i] = True
            if dfs(length, finish, add + sticks[i], i + 1, used, sticks, n):
                return True
            used[i] = False
        elif add + sticks[i] > length:
            break  # 剪枝：當前木棒太長，後面的更長

    return False


def can_form_square(sticks):
    total_sum = sum(sticks)
    max_stick = max(sticks)

    # 總和必須是4的倍數，且最長木棒不能超過邊長
    if total_sum % 4 != 0 or max_stick > total_sum // 4:
        return False

    target_length = total_sum // 4
    n = len(sticks)
    used = [False] * n

    sticks.sort(reverse=True)

    return dfs(target_length, 0, 0, 0, used, sticks, n)


def main():
    t = int(input())

    for _ in range(t):
        n = int(input())
        sticks = list(map(int, input().split()))

        if can_form_square(sticks):
            print("yes")
        else:
            print("no")


if __name__ == "__main__":
    main()
