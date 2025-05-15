import re

words = set()

while True:
    try:
        line = input().lower()
        words.update(re.findall(r"[a-z]+", line))
    except EOFError:
        break
for word in sorted(words):
    print(word)
