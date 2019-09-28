import sys

def gcd(a,b):
    if a<b:
        a,b = b,a
    if b==0:
        return a
    if a%b == 0:
        return b
    else:
        return gcd(b,a%b)

def lcm(a,b):
    return a*b//gcd(a,b)

def make_numer_and_denom(son,mom,M): #통분한 분모,분자 만들기
    numer=0
    denom=mom[0]
    for i in range(M):
        denom = lcm(denom,mom[i])    
    
    for i in range(M):
        numer += son[i]*denom//mom[i]
    return denom, numer

def result(numer,denom):
    gcd_val = gcd(denom,numer)

    if gcd_val==1: #기약분수라면
        return ((numer%mod)*pow(denom,mod-2,mod))%mod
    else : #아니면 기약분수로
        denom = denom//gcd_val
        numer = numer//gcd_val
        return ((numer%mod)*pow(denom,mod-2,mod))%mod
    
M=int(input())
lst = [[],[]]
for i in range(M):
    N, S = map(int,sys.stdin.readline().split()) #분모 N, 분자 S
    lst[0].append(N)
    lst[1].append(S)
mom = lst[0]
son = lst[1]
mod = 1000000007
b,a = make_numer_and_denom(son,mom,M) #b:분모, a:분자
print(result(a,b,mod))