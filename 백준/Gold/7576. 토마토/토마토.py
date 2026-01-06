import sys
from collections import deque

m,n=map(int,sys.stdin.readline().split())
visited=[[0]*m for _ in range(n)]
dx=[-1,1,0,0]
dy=[0,0,-1,1]
graph=[]
for i in range(n):
    graph.append(list(map(int,sys.stdin.readline().split())))

queue=deque()

# 시작 전에 모든 토마토가 익어 있는지 확인
all_ripe=True
ripe_cnt=0
for i in range(n):
    for j in range(m):
        if graph[i][j] == 1 or graph[i][j]==-1:
            ripe_cnt+=1
if ripe_cnt==m*n:
    print(0)
    sys.exit()

for i in range(n):
    for j in range(m):
        if graph[i][j]==1:
            queue.append((i,j))
            visited[i][j]=1

while queue:
    x,y=queue.popleft()
    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]
        if 0<=nx<n and 0<=ny<m:
            if graph[nx][ny]==0 and visited[nx][ny]==0:
                graph[nx][ny]=1
                queue.append((nx,ny))
                visited[nx][ny]=visited[x][y]+1
flag=True
for i in range(n):
    for j in range(m):
        if graph[i][j]==0:
            flag=False
            break

if flag==False:
    print(-1)
else:
    max_num=0
    for i in range(n):
        for j in range(m):
            if visited[i][j]>max_num:
                max_num=visited[i][j]
    print(max_num-1)