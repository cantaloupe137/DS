import math
def Prime(n):
    n = int(n)
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True
def solve(n):
    """
    如果Prime(n) return的結果是True，且n轉成字串並反轉後和n不同，n就是emirp
    若return的結果是True，但轉成字串並反轉後相同，則為Prime，但不是emirp
    若return的結果是False，那就不是Prime，也不是emirp
    (return的結果是False，後面的判斷式也不用判斷)
    """
    if Prime(n) and Prime(str(n)[n::-1]) and n != int(str(n)[n::-1]):
        #全部的條件為True
        return f'{n} is emirp.'
    #僅有Prime(n)的條件為True
    elif Prime(n):
        return f'{n} is prime.'
    else:
        return f'{n} is not prime.'
while True:
    try:
        n = int(input())
        print(solve(n))
    except EOFError:
        break