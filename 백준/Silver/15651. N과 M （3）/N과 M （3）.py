import sys

input=sys.stdin.readline
n,m= map(int,input().split())
a=list(range(1,n+1))

v=[0]*len(a)

def dfs(depth,tlst):
    if depth==m:
        print(*tlst)
        return
    for i in range(n):
        dfs(depth+1,tlst+[a[i]])

dfs(0,[])
