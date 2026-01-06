import sys

n,max_box=map(int,sys.stdin.readline().split())
m=int(sys.stdin.readline())
cost=0
packages=[]
villages=[0]*(n+1)
for _ in range(m):
    start,end,boxes=map(int,sys.stdin.readline().split())
    packages.append((start,end,boxes))
packages.sort(key=lambda x:x[1])

for i in range(m):
    start=packages[i][0]
    end=packages[i][1]
    free_space=max_box-max(villages[start:end])
    # 여유공간이 있다면, 여유 공간과 택배 중 더 작은 걸 넣기
    if free_space>0:
        box=min(free_space,packages[i][2])
        for j in range(start,end):
            villages[j]+=box
        cost+=box
print(cost)