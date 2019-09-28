import sys

N,K = map(int, sys.stdin.readline().split())
mod = 1000000007

def factorial(n):
    if n==1:
        return n
    else:
        return n*factorial(n-1)
    
a = factorial(N)
b = factorial(K)*factorial(N-K)

print(((a%mod)*pow(b,mod-2,mod))%mod)