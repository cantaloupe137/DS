T = int(input())
for t in range(T):
    n = list(map(int, input().split()))
    v = n[1:] #把第一個去掉(親戚的數量)
    v.sort()
    mid = v[n[0] // 2] #用親戚數量除以2就是中位數的索引數
    res = 0
    for i in v:
        res += abs(i - mid)
        ''' 
        如果輸入是 1, 2, 5, 999  
        -> mid = v[2] = 5 
        -> res = | 1 - 5 | + | 2 - 5 | + | 5 - 5 | + | 999 - 5 | =  1001 
        '''
    print(res)