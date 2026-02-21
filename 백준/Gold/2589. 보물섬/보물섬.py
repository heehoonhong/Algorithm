import sys
from collections import deque

dx=[-1,1,0,0]
dy=[0,0,-1,1]
input=sys.stdin.readline
n,m=map(int,input().split())
graph=[['0']*m for _ in range(n)]
visited=[[0]*m for _ in range(n)]
for i in range(n):
    line=input().strip()
    for j in range(len(line)):
        graph[i][j]=line[j]

def bfs(x,y):
    q=deque()
    q.append((x,y))
    global n,m
    visited = [[0] * m for _ in range(n)]
    visited[x][y]=1
    while q:
        cx,cy=q.popleft()
        for i in range(4):
            nx,ny=cx+dx[i],cy+dy[i]
            if 0<=nx<n and 0<=ny<m and visited[nx][ny]==0 and graph[nx][ny]=='L':
                q.append((nx,ny))
                visited[nx][ny]=visited[cx][cy]+1
    nn=0
    for i in range(n):
        for j in range(m):
            if nn<visited[i][j]:
                nn=visited[i][j]
    return nn

max_num=0
s=0
for i in range(n):
    for j in range(m):
        if visited[i][j]==0 and graph[i][j]=='L':
            s=bfs(i,j)
            if max_num<s:
                max_num=s

print(max_num-1)