def solve(n, nums):
    # 檢查是不是嚴格遞增
    for i in range(1, n):
        if nums[i] < 1 or nums[i - 1] < 1:
            return 'It is not a B2-Sequence.'
        if nums[i - 1] >= nums[i]:
            return 'It is not a B2-Sequence.'
    # seen[]存每個B[i] + B[j]的和，如果B[i] + B[j]出現在seen[]裡面的話，就不是B2-sequence
    seen = set()
    for i in range(n):
        for j in range(i, n):
            sum_value = nums[i] + nums[j]
            if sum_value in seen:
                return 'It is not a B2-Sequence.'
            seen.add(sum_value)
    return 'It is a B2-Sequence.'


count = 1
while True:
    try:
        line = input().strip()
        if not line:
            continue
        n = int(line)
        line = input().strip()
        if not line:
            print(f'Case #{count}: It is not a B2-Sequence.')
            count += 1
            continue
        nums = list(map(int, line.split()))
        print(f'Case #{count}: {solve(n, nums)}\n')
        count += 1
    except EOFError:
        break
