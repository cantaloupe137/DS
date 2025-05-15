while True:
    try:
        n = int(input())
        letter = {}

        for _ in range(n):
            line = input().upper()
            for char in line:
                if 65 <= ord(char) <= 90:
                    if char in letter:
                        letter[char] += 1
                    else:
                        letter[char] = 1
        def sorted_key(item):
            #e.g. dict = {'A':3} 則回傳 3, A
            return item[1], item[0]
        sorted_letters = sorted(letter.items(), key = sorted_key, reverse=True)
        for char, count in sorted_letters:
            print(f'{char} {count}')
    except EOFError:
        break
    except ValueError:
        break