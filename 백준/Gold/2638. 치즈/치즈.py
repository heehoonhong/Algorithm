import sys
from collections import deque

input=sys.stdin.readline
dx=[-1,1,0,0]
dy=[0,0,-1,1]
n,m=map(int,input().split())
graph=[[0]*m for _ in range(n)]
cheese_cnt=0
cnt=0
for i in range(n):
    line=list(map(int,input().split()))
    for j in range(m):
        graph[i][j]=line[j]
        if graph[i][j]==1:
            cheese_cnt+=1

def bfs():
    global cheese_cnt
    visited=[[0]*m for _ in range(n)]
    q=deque()
    q.append((0,0))
    visited[0][0]=1
    cheese_q=deque()

    while q:
        x,y=q.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<n and 0<=ny<m:
                if visited[nx][ny]==0 and graph[nx][ny]==0:
                    q.append((nx,ny))
                    visited[nx][ny]=1
                elif graph[nx][ny]==1:
                    visited[nx][ny]+=1
    for i in range(n):
        for j in range(m):
            if graph[i][j]==1 and visited[i][j]>=2:
                graph[i][j]=0
                cheese_cnt-=1


    #for i in range(n):
    #    for j in range(m):
    #        print(graph[i][j],end=' ')
    #    print()
    #print("===========")





while True:
    bfs()
    cnt+=1
    #print(cheese_cnt)
    if cheese_cnt<=0: break

print(cnt)
