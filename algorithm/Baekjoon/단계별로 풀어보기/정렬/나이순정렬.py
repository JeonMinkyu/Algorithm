import sys

N = int(sys.stdin.readline())
lst = []
for i in range(N): 
    age, name = sys.stdin.readline().split() 
    lst.append((int(age),name))
    
sorted_lst = sorted(lst, key = lambda x:x[0])
for element in sorted_lst:
    for i in element:
        print(i,end=" ")
    print("")