n = int(input())
count = {}
for _ in range(n):
    country = input().split()[0]
    count[country] = count.get(country, 0) + 1
for country, count in sorted(count.items()):
    print(f'{country} {count}')