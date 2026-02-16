import sys

input=sys.stdin.readline

n,m=map(int,input().split())
parent=list(range(n+1))
edges=[]
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

for _ in range(m):
    a,b,c=map(int,input().split())
    edges.append((a,b,c))
edges.sort(key=lambda x:x[2])

cnt=[]
for i in range(m):
    if find(edges[i][0])!=find(edges[i][1]):
        union(edges[i][0],edges[i][1])
        cnt.append(edges[i])

total=0
for i in range(len(cnt)-1):
    total+=cnt[i][2]
print(total)
