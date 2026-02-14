import sys

input=sys.stdin.readline
sys.setrecursionlimit(10**6)
n=int(input())
max_dist=0
max_node=0
graph=[[] for _ in range(n+1)]
for i in range(n-1):
    a,b,w=map(int,input().split())
    graph[a].append((b,w))
    graph[b].append((a,w))

visited=[0]*(n+1)

def dfs(node, dist):
    global max_dist,max_node
    if visited[node]==0:
        visited[node]=1

    if max_dist<dist:
        max_dist=dist
        max_node=node

    for next_node,next_weight in graph[node]:
        if visited[next_node]==0:
            dfs(next_node,dist+next_weight)

dfs(1,0)
visited=[0]*(n+1)
dfs(max_node,0)
print(max_dist)