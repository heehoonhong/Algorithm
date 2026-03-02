import sys
from collections import deque

input=sys.stdin.readline
n=int(input())
cnt=1
ans=n*n
s=0
dx=[-1,1,0,0]
dy=[0,0,-1,1]
graph=[[0]*n for _ in range(n)]
visited=[[0]*n for _ in range(n)]

def bfs(x,y):
    global cnt

    q=deque()
    q.append((x,y))
    visited[x][y]=1
    graph[x][y]=cnt
    while q:
        x,y=q.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<n and 0<=ny<n and visited[nx][ny]==0 and graph[nx][ny]==1:
                visited[nx][ny]=1
                graph[nx][ny]=cnt
                q.append((nx,ny))

def bfs2(x,y):
    global s
    visited=[[0]*n for _ in range(n)]
    # 현재 나의 도시 번호
    start=graph[x][y]
    q=deque()
    q.append((x,y))
    visited[x][y]=0

    ss=0
    while q:
        x,y=q.popleft()
        if graph[x][y]!= 0 and graph[x][y]!=start:
            ss=visited[x][y]
            break
        for i in range(4):
            nx,ny=x+dx[i],y+dy[i]
            # 바다를 건너야 해서
            if 0<=nx<n and 0<=ny<n and visited[nx][ny]==0 and (graph[nx][ny]==0 or graph[nx][ny]!=start):
                visited[nx][ny]=visited[x][y]+1
                q.append((nx,ny))

    if ss==0:
        return n*n
    else:
        return ss-1


for i in range(n):
    line=list(map(int,input().split()))
    for j in range(n):
        graph[i][j]=line[j]

for i in range(n):
    for j in range(n):
        if graph[i][j]==1 and visited[i][j]==0:
            bfs(i,j)
            cnt+=1

for i in range(n):
    for j in range(n):
        if graph[i][j]!=0:
            s=bfs2(i,j)
            ans=min(ans,s)

print(ans)