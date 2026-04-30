from collections import deque

def solution(board):
    
    n=len(board)
    m=len(board[0])
    dx=[1,-1,0,0]
    dy=[0,0,-1,1]
    xx,yy=0,0
    def bfs():
        visited=[[0]*m for _ in range(n)]
        q=deque()
        for i in range(n):
            for j in range(m):
                if board[i][j]=='R':
                    q.append((i,j))
                    visited[i][j]=1
                if board[i][j]=='G':
                    xx,yy=i,j
        cnt=0
        while q:
            x,y=q.popleft()
            if x==xx and y==yy:
                return visited[xx][yy]-1
            for i in range(4):
                nx,ny=x+dx[i],y+dy[i]
                while 0<=nx<n and 0<=ny<m and board[nx][ny]!='D':
                    nx+=dx[i]
                    ny+=dy[i]
                nx,ny=nx-dx[i],ny-dy[i]
                if 0<=nx<n and 0<=ny<m and board[nx][ny]!='D' and visited[nx][ny]==0:
                    q.append((nx,ny))
                    visited[nx][ny]=visited[x][y]+1
                    
                    
        return -1
    return bfs()
    
         