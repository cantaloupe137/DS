def solve(num):
    total = sum(i for i in range(1, num) if num % i == 0)
    if total == num:
        return "perfect"
    elif total > num:
        return "abundant"
    else:
        return "deficient"
test = int(input())
for _ in range(test):
    num = int(input())
    print(solve(num))


