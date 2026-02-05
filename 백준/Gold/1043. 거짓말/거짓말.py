import sys

input=sys.stdin.readline
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

truth=list(map(int,input().split()))
groups=[]
for _ in range(m):
    groups.append(list(map(int,input().split())))

if truth[0]==0:
    print(m)
    sys.exit()

# 진실을 아는 사람들끼리 union
for i in range(1,len(truth)):
    union(truth[1],truth[i])
cnt=0
for group in groups:
    # 1. 한 그룹에 대해서 union하고,
    # 2. 근데 그 그룹에서 union했을 때 find가 truth에 있다면
    for i in range(1,len(group)):
        union(group[1],group[i])

for group in groups:
    if find(group[1])!=find(truth[1]):
        cnt+=1

print(cnt)