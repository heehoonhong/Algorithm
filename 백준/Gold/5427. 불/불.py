import sys
from collections import deque

input=sys.stdin.readline
tc=int(input())
dx=[-1,1,0,0]
dy=[0,0,1,-1]
for _ in range(tc):
    m,n=map(int,input().split())
    tx,ty=0,0
    flag=False
    graph=[['0']*m for _ in range(n)]
    visited_f=[[0]*m for _ in range(n)]
    visited_s=[[0]*m for _ in range(n)]
    f_q=deque()
    s_q=deque()
    fflag=True
    for i in range(n):
        line=input().strip()
        for j in range(m):
            graph[i][j]=line[j]
            # 불
            if graph[i][j]=='*':
                f_q.append((i,j))
                visited_f[i][j]=1

            # 상근
            elif graph[i][j]=='@':
                if i==0 or i==n-1 or j==0 or j==m-1:
                    print(1)
                    #continue
                    fflag=False
                    break
                s_q.append((i,j))
                visited_s[i][j]=1

    while f_q and fflag:
        x,y=f_q.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<n and 0<=ny<m and visited_f[nx][ny]==0 and graph[nx][ny]!='#':
                f_q.append((nx,ny))
                visited_f[nx][ny]=visited_f[x][y]+1
    while s_q and fflag:
        x,y=s_q.popleft()
        if x==0 or x==n-1 or y==0 or y==m-1:
            tx,ty=x,y
            flag=True
            break
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<n and 0<=ny<m and visited_s[nx][ny]==0 and graph[nx][ny]=='.':
                if (visited_s[x][y]+1<visited_f[nx][ny]) or visited_f[nx][ny]==0:
                    s_q.append((nx,ny))
                    visited_s[nx][ny]=visited_s[x][y]+1
    #print(*visited_s)
    #print(*visited_f)
    if fflag:
        if flag:
            print(visited_s[tx][ty])
        else:
            print("IMPOSSIBLE")