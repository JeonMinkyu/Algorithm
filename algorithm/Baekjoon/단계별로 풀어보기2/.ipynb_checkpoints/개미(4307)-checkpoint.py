import sys
# 1. 각 위치별로 양 끝점으로 갈때의 min, max값 구함
# 2. 각 점의 min, max에 대해 max값을 구하면 min에 대한 max값은 min, max에 대한 max값은 max
def main():
    num_test_case = int(sys.stdin.readline())
    min_times = []
    max_times = []
    for i in range(num_test_case):
        l,n = map(int, sys.stdin.readline().split())
        k = [int(sys.stdin.readline()) for _ in range(n)]
        
        mintime=0
        maxtime=0
        for i in range(n):
            mini = min(k[i],l-k[i])
            maxi = max(k[i],l-k[i])

            mintime = max(mintime, mini)
            maxtime = max(maxtime, maxi)
            
        min_times.append(mintime)
        max_times.append(maxtime)

    for i in range(num_test_case):
        print(min_times[i], max_times[i])

main()