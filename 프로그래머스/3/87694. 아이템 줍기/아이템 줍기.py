from collections import deque

def solution(rectangle, characterX, characterY, itemX, itemY):
    graph=[[0]*102 for i in range(102)]
    visited=[[0]*102 for i in range(102)]
    dx=[-1,1,0,0]
    dy=[0,0,1,-1]
    
    # 1. graph 1,2 채워넣기 1은 테두리 2는 안쪽
    for each in rectangle:
        x1,y1,x2,y2=each[0]*2,each[1]*2,each[2]*2,each[3]*2
        for i in range(x1,x2+1):
            for j in range(y1,y2+1):
                if graph[i][j]==0:
                    if x1<i<x2 and y1<j<y2:
                        graph[i][j]=2
                    else:
                        graph[i][j]=1
                elif graph[i][j]==1:
                    if x1<i<x2 and y1<j<y2:
                        graph[i][j]=2 
                    else:
                        graph[i][j]=1
                else:
                    graph[i][j]=2
                            
                        
                        
    q=deque()
    q.append((characterX*2,characterY*2))
    visited[characterX*2][characterY*2]=1
    
    while q:
        x,y=q.popleft()
        for i in range(4):
            nx,ny=dx[i]+x,dy[i]+y
            if 0<=nx<=101 and 0<=ny<=101 and visited[nx][ny]==0 and graph[nx][ny]==1:
                q.append((nx,ny))
                visited[nx][ny]=visited[x][y]+1
    return (visited[itemX*2][itemY*2]-1)//2