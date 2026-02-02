import sys
from itertools import combinations_with_replacement

input=sys.stdin.readline
n,m=map(int,input().split())
a=list(map(int,input().split()))
a=set(a)
a=list(a)
a.sort()
nn=len(a)

def dfs(depth,tlst):
    if depth==m:
        result=" ".join(map(str,tlst))
        print(result)
        return
    for i in range(nn):
        if tlst==[]:
            dfs(depth+1,tlst+[a[i]])
        else:
            if tlst[-1]<=a[i]:
                dfs(depth+1,tlst+[a[i]])

dfs(0,[])
