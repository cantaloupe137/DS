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

        i = 2
        while i * i <= n:
            if n % i == 0:
                print("Not Prime")
                break
            i += 1

        else:
            print("Prime")

    except EOFError:
        break
    except ValueError:
        continue
