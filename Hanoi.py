# hanoi(n : disc數, A : 起點, B : 中繼點, C : 終點)
# 如果disc 數量 == 1, 直接把起點的移到終點
# if n == 1:
# print (move disc from A to C)
# 如果大於1，把起點的移到中繼點
# if n != 1:
# hanoi(n - 1, A , C, B)
# print(move disc n from A to B)
# hanoi(n - 1, B, A, C)
def hanoi(n, A, B, C, step=[0]):
    if n == 1:
        step[0] += 1
        print(f"Step {step[0]}")
        print(f"Move disk 1 from rod {A} to rod {C}.\n")
    else:
        hanoi(n - 1, A, C, B, step)
        step[0] += 1
        print(f"Step {step[0]}")
        print(f"Move disk {n} from rod {A} to rod {B}.\n")
        hanoi(n - 1, C, B, A, step)


while True:
    try:
        n = int(input())
        if n == 0:
            break
        step = [0]
        hanoi(n, 'A', 'B', 'C', step)
        print(f"Total moved {step[0]} steps.\n")
    except EOFError:
        break
