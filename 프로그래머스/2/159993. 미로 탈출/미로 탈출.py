from collections import deque

def solution(maps):
    # 통로 or 벽
    # 통로에 문이 있음
    # 문에는 레버가 있음
    n=len(maps)
    m=len(maps[0])
    dx=[-1,1,0,0]
    dy=[0,0,1,-1]
    start,end,door=0,0,0
    for i in range(n):
        for j in range(m):
            if maps[i][j]=='S':
                start=(i,j)
            elif maps[i][j]=='E':
                end=(i,j)
            elif maps[i][j]=='L':
                door=(i,j)
    def bfs(first,second):
        visited=[[0]*m for _ in range(n)]
        q=deque()
        sx,sy=first
        ex,ey=second
        
        q.append((sx,sy))
        visited[sx][sy]+=1
        
        while q:
            x,y=q.popleft()
            if x==ex and y==ey:
                #print(visited[x][y]-1)
                return visited[x][y]-1
            for i in range(4):
                nx=x+dx[i]
                ny=y+dy[i]
                if 0<=nx<n and 0<=ny<m and visited[nx][ny]==0 and maps[nx][ny]!='X':
                    q.append((nx,ny))
                    visited[nx][ny]=visited[x][y]+1
        return 0
        
    s1=bfs(start,door)
    s2=bfs(door,end)
    if s1!=0 and s2!=0:
        return s1+s2
    else:
        return -1