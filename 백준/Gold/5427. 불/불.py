import sys
from collections import deque

input=sys.stdin.readline
dx=[-1,1,0,0]
dy=[0,0,-1,1]
tc=int(input())

for _ in range(tc):
    flag=False
    ans = 0
    f_q=deque()
    s_q=deque()
    n,m=map(int,input().split())
    graph=[['0']*n for _ in range(m)]
    visited_f = [[-1] * n for _ in range(m)]
    visited_s = [[-1] * n for _ in range(m)]
    for i in range(m):
        line=input().strip()
        for j in range(n):
            graph[i][j]=line[j]
            if graph[i][j]=='*':
                f_q.append((i,j))
                visited_f[i][j]=0
            elif graph[i][j]=='@':
                s_q.append((i,j))
                visited_s[i][j]=0
                if i==0 or i==m-1 or j==0 or j==n-1:
                    flag=True

    # 불, 상준이에 대해서 두 번 BFS를 돌림
    # i,j 에 대해서 visited_f>=visited_s이어야 함.
    # 불: 네 방향 미방문, 벽이 아닌 곳
    # 상준: 네 방향 미방문, 빈 공간만 이동 가능


    # 불 먼저 진행
    while f_q:
        x,y=f_q.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<m and 0<=ny<n and visited_f[nx][ny]==-1 and graph[nx][ny]!='#':
                f_q.append((nx,ny))
                visited_f[nx][ny]=visited_f[x][y]+1

    while s_q:
        x,y=s_q.popleft()

        if x==0 or x==m-1 or y==0 or y==n-1:
            ans=visited_s[x][y]
            break
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<m and 0<=ny<n and visited_s[nx][ny]==-1 and graph[nx][ny]=='.':
                # 불이 아예 안 오는 곳도 처리해야 함, 불이 안 올 수도 있으니까... 
                if visited_s[x][y]+1<visited_f[nx][ny] or visited_f[nx][ny]==-1:
                    s_q.append((nx,ny))
                    visited_s[nx][ny]=visited_s[x][y]+1
    if flag==True:
        print(1)
    else:
        if ans==0:
            print("IMPOSSIBLE")
        else:
            print(ans+1)