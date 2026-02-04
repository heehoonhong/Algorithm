import sys

sys.setrecursionlimit(10**6)
input=sys.stdin.readline
n=int(input())
a=list(range(n+1))
parent=list(range(n+1))

def find(x):
    if parent[x]==x:
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

m=int(input())
for i in range(1,n+1):
    ss=[0]+list(map(int,input().split()))
    for j in range(1,n+1):
        if ss[j]==1:
            union(i,j)

ss=list(map(int,input().split()))
flag=True
temp=parent[ss[0]]
for i in range(1,len(ss)):
    if temp != parent[ss[i]]:
        flag=False
        break
if not flag:
    print("NO")
else:
    print("YES")