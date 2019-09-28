import sys
# 1. 패키지 중 최솟값, 낱개 가격 중 최솟값 각각 구함
# 2.
# 1) N<=6 : 패키지 1개, N*낱개가격 비교
# 2) N>6
    # 1) 패키지 + 낱개가격
    # 2) 패키지
    # 3) 낱개 비교
N,M = map(int, sys.stdin.readline().split())
cost = [[],[]]
for i in range(M):
    a_0, a_1 = map(int,sys.stdin.readline().split())
    cost[0].append(a_0)
    cost[1].append(a_1)

# 1.
min_pack = min(cost[0])
min_per = min(cost[1])

# 2.
if N<=6: # 1)
    total = min(min_pack, min_per*N)    
else: # 2)
    a = (N//6)*min_pack + (N%6)*min_per # 1)
    b = ((N//6)+1)*min_pack # 2)
    c = N*min_per # 3)
    total = min(a,b,c)

print(total)