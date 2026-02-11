import sys
from collections import deque

input=sys.stdin.readline
n,m,v=map(int,input().split())
graph=[[] for _ in range(n+1)]
for _ in range(m):
    a,b=map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(1,n+1):
    graph[i].sort()

def dfs(v):
    if visited[v]==0:
        visited[v]=1
        ans_dfs.append(v)

    for next_node in graph[v]:
        if visited[next_node]==0:
            dfs(next_node)

def bfs(v):
    q=deque()
    visited[v]=1
    q.append(v)
    ans_bfs.append(v)
    while q:
        node=q.popleft()
        for next_node in graph[node]:
            if visited[next_node]==0:
                visited[next_node]=1
                q.append(next_node)
                ans_bfs.append(next_node)

ans_dfs=[]
ans_bfs=[]
visited=[0]*(n+1)
dfs(v)
visited=[0]*(n+1)
bfs(v)
print(*ans_dfs)
print(*ans_bfs)
