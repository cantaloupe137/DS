from Bangla_Numbers import solve


def test_bangla_numbers():
    """測試孟加拉數字轉換功能"""

    # 測試用例
    test_cases = [
        (0, "zero"),
        (1, "one"),
        (10, "ten"),
        (15, "fifteen"),
        (20, "twenty"),
        (25, "twenty five"),
        (100, "one shata"),
        (150, "one shata fifty"),
        (1000, "one hajar"),
        (1500, "one hajar five shata"),
        (100000, "one lakh"),
        (150000, "one lakh five hajar"),
        (10000000, "one kuti"),
        (15000000, "one kuti five lakh"),
        (999999999999999, "nine shata ninety nine kuti nine shata ninety nine lakh nine shata ninety nine hajar nine shata ninety nine"),
    ]

    print("測試孟加拉數字轉換：")
    print("=" * 50)

    for i, (number, expected) in enumerate(test_cases, 1):
        result = solve(number)
        status = "✓" if result == expected else "✗"
        print(f"測試 {i}: {number}")
        print(f"  期望: {expected}")
        print(f"  結果: {result}")
        print(f"  狀態: {status}")
        print()


if __name__ == "__main__":
    test_bangla_numbers()
