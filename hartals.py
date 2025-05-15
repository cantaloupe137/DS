def solve(days, party):
    # set不會重複算已經加進去的罷工日子數
    no_work = set()
    for i in party:
        temp = i  # 從第i天罷工
        while temp <= days:
            # working days exclude Sat and Sun
            if temp % 7 != 6 and temp % 7 != 0:
                no_work.add(temp)  # 紀錄罷工的日子
            temp += i  # 下次罷工日是i天後
    return len(no_work)  # 回傳沒有工作的日子


T = int(input())
for t in range(T):
    days = int(input())
    party = []
    for i in range(int(input())):
        party.append(int(input()))
    print(solve(days, party))
