while True:
    try:
        nline = input()
        if not nline.strip():
            continue
        n = int(nline)
        letter = {}
        for _ in range(n):
            line = input().upper()
            for char in line:
                if 'A' <= char <= 'Z':
                    letter[char] = letter.get(char, 0) + 1
        sorted_letters = sorted(letter.items(), key=lambda item: (-item[1], item[0]))
        for char, count in sorted_letters:
            print(f"{char} {count}")
    except EOFError:
        break
    except ValueError:
        break