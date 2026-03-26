from collections import deque

def solution(storage, requests):
    # requests[i]==1일 때는 접근 가능한 알파벳들만 없애기
    # requests[i]==2일 때는 그 알파벳에 해당하는 모든 위치들에 대해서 없애기
    n=len(storage)
    m=len(storage[0])
    dx=[0,0,1,-1]
    dy=[1,-1,0,0]
    graph=[['0']*m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            graph[i][j]=storage[i][j]
    
    
    def can_reach(tx,ty):
        if tx==0 or tx==n-1 or ty==0 or ty==m-1: return True
        visited=[[0]*m for _ in range(n)]
        q=deque()
        for i in range(n):
            if graph[i][0]=='0':
                q.append((i,0))
                visited[i][0]=1
            if graph[i][m-1]=='0':
                q.append((i,m-1))
                visited[i][m-1]=1
        
        for j in range(m):
            if graph[0][j]=='0':
                q.append((0,j))
                visited[0][j]=1
            if graph[n-1][j]=='0':
                q.append((n-1,j))
                visited[n-1][j]=1
            
    
        # q에서 하나씩 pop하면서
        # 상하좌우에 tx,ty인지 탐색하고
        # q에 append하는 건 빈 공간만 append
        while q:
            x,y=q.popleft()
            # tx, ty 찾기
            for i in range(4):
                nx,ny=x+dx[i],y+dy[i]
                if 0<=nx<n and 0<=ny<m and (nx==tx and ny==ty) and graph[nx][ny]!='0':
                    return True
            
            for i in range(4):
                nx,ny=x+dx[i],y+dy[i]
                if 0<=nx<n and 0<=ny<m and visited[nx][ny]==0 and graph[nx][ny]=='0':
                    visited[nx][ny]=1
                    q.append((nx,ny))
        return False
            
            
    
    for index in range(len(requests)):
        # 이렇게 s를 둬서 하는 이유는 
        # 길이가 1일 때는 한 개만 빼내야 하는데
        # 도달 가능할 때 '0'으로 바꿔버린다면 
        # 그 턴에 계속해서 그 알파벳을 삭제해 버려서 틀렸음
        # 따라서 s에 모아서 한꺼번에 처리해야 함.
        s=[]
        if len(requests[index])==1:
            
            for i in range(n):
                for j in range(m):
                    if graph[i][j]==requests[index][0] and can_reach(i,j):
                        s.append((i,j))
                    
        else:
            for i in range(n):
                for j in range(m):
                    if graph[i][j]==requests[index][0]:
                        #graph[i][j]='0'
                        s.append((i,j))
        for (xx,yy) in s:
            graph[xx][yy]='0'
    result=0
    for i in range(n):
        for j in range(m):
            if graph[i][j]!='0': result+=1
    return result