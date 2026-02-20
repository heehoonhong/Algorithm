import sys
from collections import deque

input=sys.stdin.readline
n,m=map(int,input().split())
cnt=0
cheese_cnt=0
dx=[-1,1,0,0]
dy=[0,0,-1,1]
graph=[[0]*m for _ in range(n)]
visited=[[0]*m for _ in range(n)]
for i in range(n):
    a=list(map(int,input().split()))
    for j in range(m):
        graph[i][j]=a[j]
        if graph[i][j]==1:
            cheese_cnt+=1


def bfs():
    global n,m,graph,cheese_cnt
    current_cheese=0
    q=deque()
    q.append((0,0))
    cheese_q=deque()
    visited=[[0]*m for _ in range(n)]
    while q:
        x,y=q.popleft()
        for i in range(4):
            nx=dx[i]+x
            ny=dy[i]+y
            if 0<=nx<n and 0<=ny<m and visited[nx][ny]==0:
                #  빈 공간
                if graph[nx][ny]==0:
                    q.append((nx,ny))
                    visited[nx][ny]=1

                # 치즈
                elif graph[nx][ny]==1:
                    current_cheese+=1
                    visited[nx][ny]=1
                    graph[nx][ny]=0
                    cheese_cnt-=1

    return current_cheese

answer=0
while True:
    cnt += 1
    s=bfs()
    if cheese_cnt<=0:
        answer=s
        break

print(cnt)
print(answer)