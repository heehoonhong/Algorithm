import sys
from collections import defaultdict

input=sys.stdin.readline
n=int(input())
memo=defaultdict(int)
memo[1],memo[2]=1,1

def f(n):
    if n<=2:
        return 1%1000000007
    else:
        if memo[n]>0:
            return memo[n]

        half=n//2
        if n%2==0:
            h0=f(half)
            h1=f(half-1)
            memo[n]=(h0**2+2*h0*h1)%1000000007
            return memo[n]
        else:
            h0=f(half)
            h1=f(half+1)
            memo[n]=(h0**2+h1**2)%1000000007
            return memo[n]

print(f(n))
