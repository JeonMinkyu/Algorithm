# import sys

# A = int(sys.stdin.readline())
# X = int(sys.stdin.readline())
# mod = 1000000007
# total = 1

# indices=[]
# i=1
# x=X
# if x%2==1: #첫번째
#     indices.append(2**0)
# while x>1:
#     x = x//2
#     if x%2 == 1:
#         indices.append(2**i)
#     i=i+1

# A_dic = {}
# x=1
# per_A = A
# t = 1
# for indice in indices:
#     t = indice//t
#     per_A = per_A**t
#     A_dic[indice]=per_A
#     t = indice

# for indice in indices:
#     out = A_dic[indice]%mod
#     total = total*out
# print(total%mod)
import sys
print(pow(int(sys.stdin.readline()),int(sys.stdin.readline()),10**9+7))

