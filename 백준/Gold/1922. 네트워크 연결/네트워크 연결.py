import sys

input=sys.stdin.readline
n=int(input())
m=int(input())
parent=list(range(n+1))
edges=[]
for _ in range(m):
    a,b,c=map(int,input().split())
    edges.append((a,b,c))
def find(x):
    if x==parent[x]:
        return x
    else:
        # 재귀적으로 parent[x] 호출하기
        parent[x]=find(parent[x])
    return parent[x]

def union(a,b):
    parent_a=find(a)
    parent_b=find(b)
    # 작은 쪽에 합치기
    if parent_a<parent_b:
        parent[parent_b]=parent_a
    else:
        parent[parent_a]=parent_b

edges.sort(key=lambda x:x[2])
total=0

for i in range(m):
    if find(edges[i][0]) != find(edges[i][1]):
        union(edges[i][0],edges[i][1])
        total+=edges[i][2]

print(total)
