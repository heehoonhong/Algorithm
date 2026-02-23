import sys
from collections import deque

input=sys.stdin.readline
n,m=map(int,input().split())
graph=[['0']*m for _ in range(n)]
visited=[[0]*m for _ in range(n)]
dx=[-1,1,0,0]
dy=[0,0,-1,1]
target=deque()
q=deque()
cnt=0
for i in range(n):
    line=input().strip()
    for j in range(m):
        graph[i][j]=line[j]
        if graph[i][j]=='.':
            cnt+=1
        if graph[i][j]=='D':
            target.append((i,j))
            cnt+=1

def bfs():
    global cnt
    q=deque()
    for i in range(n):
        for j in range(m):
            if graph[i][j]=='*':
                q.appendleft((i,j))
            elif graph[i][j]=='S':
                q.append((i,j))

    while q:
        x,y=q.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<n and 0<=ny<m and visited[nx][ny]==0:
                if graph[x][y]=='*':
                    if graph[nx][ny]=='.':
                        visited[nx][ny]=visited[x][y]+1
                        graph[nx][ny]='*'
                        cnt-=1
                if graph[x][y]=='S':
                    if graph[nx][ny]=='.':
                        visited[nx][ny]=visited[x][y]+1
                        graph[nx][ny]='S'
                        cnt-=1
                    elif graph[nx][ny]=='D':
                        visited[nx][ny]=visited[x][y]+1
                        graph[nx][ny]='S'
                        cnt-=1
dd=0
while dd<n*m:
    bfs()
    dd+=1

    if cnt<=0:break

tx,ty=target.popleft()
if visited[tx][ty]==0:
    print("KAKTUS")
else:
    print(visited[tx][ty])