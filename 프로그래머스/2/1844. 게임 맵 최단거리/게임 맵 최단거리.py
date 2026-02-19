from collections import deque

def solution(maps):
    n=len(maps)
    m=len(maps[0])
    visited=[[0]*m for _ in range(n)]
    answer=0
    
    dx=[-1,1,0,0]
    dy=[0,0,-1,1]
    
    def bfs(x,y):
        nonlocal answer
        nonlocal n
        nonlocal m
        q=deque()
        q.append((x,y))
        visited[x][y]=1
        
        while q:
            cx,cy=q.popleft()
            for i in range(4):
                nx=dx[i]+cx
                ny=dy[i]+cy
                if 0<=nx<n and 0<=ny<m and visited[nx][ny]==0 and maps[nx][ny]==1:
                    q.append((nx,ny))
                    visited[nx][ny]=visited[cx][cy]+1
        answer=visited[-1][-1]
    
    bfs(0,0)
    if answer==0:
        return -1
    else:
        return answer