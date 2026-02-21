import sys

input=sys.stdin.readline
n,m=map(int,input().split())
a=[]
for i in range(n):
    arr=list(map(int,input().split()))
    a.append(arr)

m,k=map(int,input().split())
b=[]
for i in range(m):
    arr=list(map(int,input().split()))
    b.append(arr)
result=[[0]*k for _ in range(n)]
for i in range(n):
    for j in range(k):
        for kk in range(m):
            result[i][j]+=a[i][kk]*b[kk][j]
    print(*result[i])
