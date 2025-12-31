import sys
from collections import deque

queue=deque()
dx=[-1,1,0,0]
dy=[0,0,-1,1]

n,m=map(int,sys.stdin.readline().split())

graph=[list(map(int,sys.stdin.readline().strip())) for _ in range(n)]
visited=[[0]*m for _ in range(n)]

queue.append((0,0))
visited[0][0]=1

while queue:
    x,y=queue.popleft()
    #visited[x][y]=1
    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]
        if 0 <= nx < n and 0 <= ny < m:
            if graph[nx][ny]==1 and visited[nx][ny]==0:
                visited[nx][ny]=visited[x][y]+1
                queue.append((nx,ny))
print(visited[n-1][m-1])