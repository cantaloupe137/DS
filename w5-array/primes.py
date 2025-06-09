import math

while True:
    try:
        n = int(input())

        if n <= 1:
            print("Not Prime")
            continue

        if n == 2:
            print("Prime")
            continue

        if n % 2 == 0:
            print("Not Prime")
            continue

        is_prime = True
        for i in range(3, int(math.sqrt(n)) + 1, 2):
            if n % i == 0:
                print("Not Prime")
                is_prime = False
                break

        if is_prime:
            print("Prime")

    except EOFError:
        break
    except ValueError:
        continue
