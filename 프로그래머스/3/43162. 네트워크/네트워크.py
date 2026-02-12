def solution(n, computers):
    visited=[0]*n
    cnt=0
    graph=[[] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if i!=j and computers[i][j]==1:
                graph[i].append(j)
                graph[j].append(i)
    
    def dfs(v):
        if visited[v]==0:
            visited[v]=1
        for next_node in graph[v]:
            if visited[next_node]==0:
                dfs(next_node)
    
    
    for i in range(n):
        if visited[i]==0:
            dfs(i)
            cnt+=1
    
    
    return cnt