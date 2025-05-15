def is_prime(n):
    if n < 2:
        return False
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return True

T = int(input().strip())

for case_num in range(1, T + 1):
    s = input().strip()

    freq = {}
    for ch in s:
        if ch in freq:
            freq[ch] += 1
        else:
            freq[ch] = 1

    prime_chars = sorted(ch for ch in freq if is_prime(freq[ch]))

    if prime_chars:
        print(f"Case {case_num}: {''.join(prime_chars)}")
    else:
        print(f"Case {case_num}: empty")

