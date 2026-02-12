from collections import deque

def solution(n, computers):
    visited=[0]*n
    cnt=0
    graph=[[] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if i!=j and computers[i][j]==1:
                graph[i].append(j)
                graph[j].append(i)
    
    def bfs(v):
        q=deque()
        q.append(v)
        visited[v]=1
        
        while q:
            node=q.popleft()
            for next_node in graph[node]:
                if visited[next_node]==0:
                    q.append(next_node)
                    visited[next_node]=1
    
    for i in range(n):
        if visited[i]==0:
            bfs(i)
            cnt+=1
    
    
    return cnt