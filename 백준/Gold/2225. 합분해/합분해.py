import sys

n,k=map(int,sys.stdin.readline().split())
b=1
a=1
for i in range(1,k):
    b*=i
    a*=(n+i)
print((a//b)%1000000000)