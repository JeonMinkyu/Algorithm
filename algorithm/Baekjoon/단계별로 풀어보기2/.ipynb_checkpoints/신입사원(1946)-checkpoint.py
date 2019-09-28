import sys

T = int(sys.stdin.readline())
final = []
for _ in range(T):
    A = []
    N = int(sys.stdin.readline())
    for i in range(N):
        a_0,a_1 = map(int, sys.stdin.readline().split())
        A.append([a_0,a_1])
    sorted_A = sorted(A)

    first_order = 100000
    num = 0
    for score in sorted_A:
        if score[1] < first_order:
            first_order = score[1]

        if score[0] == 1 or score[1] == 1: 
            num += 1
            continue
        if score[1] > first_order:
            continue
        num+=1
    final.append(num)

for i in range(T):
    print(final[i])