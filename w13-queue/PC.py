# throwing cards away
while True:
    try:
        n = int(input())
        all = []
        D = []
        if n != 0 and n != 1:
            for i in range(1, n + 1):
                all.append(i)
            for i in range(n - 2):
                D.append(all[0])
                del all[0]
                all.append(all[0])
                del all[0]
            D.append(all[0])
            del all[0]
            print('Discarded cards:', end=' ')
            for i in range(len(D) - 1):
                print(D[i], end=', ')
            print(D[len(D) - 1])
            print('Remaining card:', all[0])
        elif n == 0:
            break
        elif n == 1:
            print('Discarded cards: ')
            print('Remaining card: 1')
    except EOFError:
        break
