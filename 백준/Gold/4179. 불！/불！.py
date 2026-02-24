import sys
from collections import deque

input=sys.stdin.readline
n,m=map(int,input().split())
dx=[-1,1,0,0]
dy=[0,0,-1,1]
graph=[['0']*m for _ in range(n)]
visited_f=[[-1]*m for _ in range(n)]
visited_j=[[-1]*m for _ in range(n)]
f_q=deque()
j_q=deque()
for i in range(n):
    line=input().strip()
    for j in range(m):
        graph[i][j]=line[j]
        if graph[i][j]=='J':
            j_q.append((i,j))
            visited_j[i][j]=0
            if i==0 or i==n-1 or j==0 or j==m-1:
                print(1)
                sys.exit()
        elif graph[i][j]=='F':
            f_q.append((i,j))
            visited_f[i][j]=0
# f bfs 실행

while f_q:
    x,y=f_q.popleft()
    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]
        if 0<=nx<n and 0<=ny<m and visited_f[nx][ny]==-1 and graph[nx][ny]!='#':
            f_q.append((nx,ny))
            visited_f[nx][ny]=visited_f[x][y]+1
flag=False
tx,ty=0,0
while j_q:
    x,y=j_q.popleft()

    if x==0 or x==n-1 or y==0 or y==m-1:
        flag=True
        tx,ty=x,y
        break
    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]
        if 0<=nx<n and 0<=ny<m and visited_j[nx][ny]==-1 and graph[nx][ny]=='.' :
            if ((visited_j[x][y]+1)<visited_f[nx][ny]) or visited_f[nx][ny]==-1:
                j_q.append((nx,ny))
                visited_j[nx][ny]=visited_j[x][y]+1

#print(*visited_f)
#print(*visited_j)

if flag:
    print(visited_j[tx][ty]+1)
else:
    print("IMPOSSIBLE")