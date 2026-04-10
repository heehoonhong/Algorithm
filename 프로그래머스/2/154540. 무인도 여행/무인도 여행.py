from collections import deque

def solution(maps):
    n=len(maps)
    m=len(maps[0])
    answer=[]
    visited=[[0]*m for _ in range(n)]
    dx=[-1,1,0,0]
    dy=[0,0,-1,1]
    
    def bfs(x,y):
        s=0
        q=deque()
        q.append((x,y))
        visited[x][y]=1
        s+=int(maps[x][y])
        
        while q:
            x,y=q.popleft()
            for i in range(4):
                nx=x+dx[i]
                ny=y+dy[i]
                if 0<=nx<n and 0<=ny<m and maps[nx][ny]!='X' and visited[nx][ny]==0:
                    q.append((nx,ny))
                    visited[nx][ny]=1
                    s+=int(maps[nx][ny])
        return s
        
        
    
    for i in range(n):
        for j in range(m):
            if maps[i][j]!='X' and visited[i][j]==0:
                num=bfs(i,j)
                answer.append(num)
    
    
    answer.sort()
    if answer==[]: return [-1]
    else: return answer
    