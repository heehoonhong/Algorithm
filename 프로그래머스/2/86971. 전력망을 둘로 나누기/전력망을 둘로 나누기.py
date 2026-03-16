from collections import deque

def solution(n, wires):
    ans=n+2
    graph=[[] for _ in range(n+1)]
    for i in range(len(wires)):
        a,b=wires[i][0],wires[i][1]
        graph[a].append(b)
        graph[b].append(a)
    
    def dfs(visited,cur):
        visited[cur]=1
        cnt=1
        
        for next_node in graph[cur]:
            if visited[next_node]==0:
                cnt+=dfs(visited,next_node)
        return cnt
    
    def bfs(visited,start):
        q=deque()
        q.append(start)
        visited[start]=1
        cnt=1
        while q:
            cur=q.popleft()
            for next_node in graph[cur]:
                if visited[next_node]==0:
                    q.append(next_node)
                    visited[next_node]=1
                    cnt+=1
        return cnt
    
    for i in range(len(wires)):
        a,b=wires[i][0],wires[i][1]
        graph[a].remove(b)
        graph[b].remove(a)
        visited=[0]*(n+1)
        visited[a]=1
        #s=dfs(visited,a)
        s=bfs(visited,a)
        result1,result2=s,n-s
        ans=min(ans,abs(result1-result2))
        graph[a].append(b)
        graph[b].append(a)
    
    return ans