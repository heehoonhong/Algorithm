import sys
import math

input=sys.stdin.readline
n=int(input())
parent=list(range(n+1))

# 자신의 조상 찾기
def find(x):
    if x==parent[x]:
        return x
    else:
        parent[x]=find(parent[x])
    return parent[x]

def union(a,b):
    parent_a=find(a)
    parent_b=find(b)
    if parent_a<parent_b:
        parent[parent_b]=parent_a
    else:
        parent[parent_a]=parent_b
stars=[]
for _ in range(n):
    x,y=map(float,input().split())
    stars.append((x,y))
edges=[]
for i in range(n):
    for j in range(i+1,n):
        xx=stars[i][0]-stars[j][0]
        yy=stars[i][1]-stars[j][1]
        edges.append((i,j,(math.sqrt(xx**2+yy**2))))

edges.sort(key=lambda x:x[2])

total=0
for i in range(len(edges)):
    if find(edges[i][0])!=find(edges[i][1]):
        union(edges[i][0],edges[i][1])
        total+=edges[i][2]

print(round(total,2))