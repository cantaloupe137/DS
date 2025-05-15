#sort sort sort
def solve(n, m, nums):
    """
            1. 數字按照它們除以 M 的餘數升序排列。
            2. 如果兩個數的餘數相同，奇數要排在偶數前面。
            3. 如果兩個數的餘數相同且都是奇數，則數值較大的排在前面。
            4. 如果兩個數的餘數相同且都是偶數，則數值較小的排在前面。
    """
    #哥們的 https://stackoverflow.com/a/46969300
    def mod(a, b):
        #算絕對值的mod
        res = abs(a) % abs(b)
        #a < 0的話，結果為正
        if a < 0:
            res *= -1
        return res
    def sort_key(x):
        """
        1. 數字按照它們除以 M 的餘數升序排列
        mod(x, m)
        2. 如果兩個數的餘數相同，奇數要排在偶數前面
        x % 2 == 0
        如果為真(1), 偶數就會排在奇數後面，因為False會在True前面
        3. 如果兩個數的餘數相同且都是奇數，則數值較大的排在前面。
        4. 如果兩個數的餘數相同且都是偶數，則數值較小的排在前面。
        -x if x % 2 != 0 else x
        x是奇數時，用 -x
        在比較時，較大的數會有更小的負值，因此會排在前面
        """
        return mod(x, m), x % 2 == 0, -x if x % 2 != 0 else x

    ans = sorted(nums, key=sort_key)
    return '\n'.join(map(str, ans))

while True:
    try:
        n ,m = list(map(int, input().split()))
        print(f'{n} {m}')
        if n == 0 and m == 0:
            break
        nums = []
        for i in range(n):
            nums.append(int(input()))
        print(solve(n, m, nums))
    except EOFError:
        break
