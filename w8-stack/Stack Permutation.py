def factorial(n):
    """計算階乘"""
    if n <= 1:
        return 1
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


def catalan_number(n):
    """計算第 n 個卡特蘭數"""
    if n <= 0:
        return 1
    # 卡特蘭數公式: C(n) = (2n)! / ((n+1)! * n!)
    numerator = factorial(2 * n)
    denominator = factorial(n + 1) * factorial(n)
    return numerator // denominator


def solve_stack_permutation():
    """解決 Stack Permutation 問題"""
    try:
        while True:
            # 讀取輸入
            n = int(input())
            # 計算並輸出結果
            result = catalan_number(n)
            print(result)
    except EOFError:
        # 當沒有更多輸入時結束
        pass
    except ValueError:
        # 處理無效輸入
        pass


if __name__ == "__main__":
    solve_stack_permutation()
