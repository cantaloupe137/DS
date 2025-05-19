def bubble_sort(n, lst, res):
    res = 0
    for i in range(n):
        for j in range(n - i - 1):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
                res += 1
    return res


while True:
    try:
        n = int(input())
        nums = list(map(int, input().split()))
        res = bubble_sort(n, nums, 0)
        print(f'Minimum exchange operations :{res}')
    except EOFError:
        break
