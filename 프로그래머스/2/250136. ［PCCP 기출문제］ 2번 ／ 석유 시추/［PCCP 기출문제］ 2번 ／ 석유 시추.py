from collections import deque

def solution(graph):
    dx=[0,0,1,-1]
    dy=[1,-1,0,0]
    n=len(graph)
    m=len(graph[0])
    visited=[[0]*m for _ in range(n)]
    # 열별 시추 가능한 석유의 양
    lst=[0]*m
    
    def bfs(x,y):
        
        temp_lst=set()
        q=deque()
        cnt=0
        q.append((x,y))
        visited[x][y]=1
        cnt+=1
        temp_lst.add(y)
        while q:
            x,y=q.popleft()
            for i in range(4):
                nx,ny=x+dx[i],y+dy[i]
                if 0<=nx<n and 0<=ny<m and visited[nx][ny]==0 and graph[nx][ny]==1:
                    visited[nx][ny]=1
                    q.append((nx,ny))
                    cnt+=1
                    temp_lst.add(ny)
        #print(temp_lst,cnt)
        return temp_lst,cnt
        
    
    for i in range(n):
        for j in range(m):
            if visited[i][j]==0 and graph[i][j]==1:
                ss,num=bfs(i,j)
                for s in ss:
                    lst[s]+=num
    #print(lst)
    result=0
    for j in range(m):
        if result<lst[j]:
            result=lst[j]
    return result