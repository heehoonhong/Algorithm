import sys

input=sys.stdin.readline
n,m= map(int,input().split())
a=list(range(1,n+1))

v=[0]*len(a)
def dfs(depth,start,tlst):
    if depth==m:
        print(*tlst)
        return
    for i in range(start,n):
        if v[i]==0:
            v[i]=1
            dfs(depth+1,i+1,tlst+[a[i]])
            v[i]=0

dfs(0,0,[])