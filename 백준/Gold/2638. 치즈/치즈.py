import sys
from collections import deque

input=sys.stdin.readline
n,m=map(int,input().split())
cheese_cnt=0
dx=[-1,1,0,0]
dy=[0,0,-1,1]
# 0이면 방문 처리하고, nx,ny 가 1이라면 이전 것들이 다 0일테니까 visited를 통해
# 방문 처리를 하고, 1 중에서 visited가 2이상이면 외부 공기와 2면 이상 접촉한 거임

graph=[[0]*m for _ in range(n)]
for i in range(n):
    line=list(map(int,input().split()))
    for j in range(m):
        graph[i][j]=line[j]
        if graph[i][j]==1:
            cheese_cnt+=1

def bfs():
    global cheese_cnt
    q=deque()
    q.append((0,0))
    visited=[[0]*m for _ in range(n)]
    cheese_q=deque()
    visited[0][0]=1

    while q:
        x,y=q.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<n and 0<=ny<m:
                if visited[nx][ny]==0 and graph[nx][ny]==0:
                    q.append((nx,ny))
                    visited[nx][ny]=1
                if graph[nx][ny]==1:
                    # 이렇게 하면 방문 처리를 안 해서 중복으로 nx,ny 좌표가 담길 수 있음
                    # 이렇게 하는 것보단 다시 전부를 돌면서 2 이상인 걸 처리하면 될 듯? 
                    cheese_q.append((nx,ny))
                    visited[nx][ny]+=1
    cheese_q=deque(set(cheese_q))
    while cheese_q:
        x,y=cheese_q.popleft()
        if visited[x][y]>=2:
            graph[x][y]=0
            cheese_cnt-=1
    #print(cheese_cnt)
    #print(*graph)

cnt=0
while True:

    bfs()
    cnt+=1
    #print(cnt)
    if cheese_cnt<=0:
        break

print(cnt)
