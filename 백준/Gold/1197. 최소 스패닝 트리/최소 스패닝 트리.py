import sys

input=sys.stdin.readline
sys.setrecursionlimit(10**6)
n,m=map(int,input().split())
parent=list(range(n+1))
a_list=list(range(n+1))
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
    if parent_a!=parent_b:
        # 작은 쪽에 합치기
        if parent_a<parent_b:
            parent[parent_b]=parent_a
        else:
            parent[parent_a]=parent_b

for _ in range(m):
    a,b,c=map(int,input().split())
    edges.append((a,b,c))

edges.sort(key=lambda x:x[2])

cnt=0
index=0
total=0
while cnt<n-1 and index<m:
    if find(edges[index][0])!= find(edges[index][1]):
       union(edges[index][0],edges[index][1])
       total+=edges[index][2]
       cnt+=1
    index+=1

print(total)