import sys

### 필요한 동전 갯수의 최솟값
# 1. 리스트에서 맨 끝부터 K보다 작은 것 중 최댓값 구함
# 2. K를 그 최댓값으로 나눈 몫과 나머지를 구하고 몫은 num, 나머지는 K
# 3. 1,2 반복

N,K = map(int, sys.stdin.readline().split())
A = [int(sys.stdin.readline()) for _ in range(N)]

def main(N,A,K):
    num=0
    while K>0: # 3.
        for i in range(N-1,-1,-1): # 1.
            if K>=A[i]:
                num = num + K//A[i] # 2.
                K = K % A[i]
                A = A[:i]
    print(num)
main(N,A,K)