import sys

input=sys.stdin.readline
sys.setrecursionlimit(10**6)
n,m=map(int,input().split())
a=list(range(n+1))
parent=list(range(n+1))
def find(x):
    if x==parent[x]:
        return x
    else:
        parent[x]=find(parent[x])
    return parent[x]

def union(x,y):
    parent_x=find(x)
    parent_y=find(y)
    if parent_x<parent_y:
        parent[parent_y]=parent_x
    else:
        parent[parent_x]=parent_y
for _ in range(m):
    c,a,b=map(int,input().split())
    if c==0:
        union(a,b)
    elif c==1:
        parent_a=find(a)
        parent_b=find(b)
        if parent_a==parent_b:
            print("YES")
        else:
            print("NO")