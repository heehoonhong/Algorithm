import sys

sys.setrecursionlimit(10**6)
input=sys.stdin.readline
n=int(input())
graph=[[] for _ in range(n+1)]
visited=[0]*(n+1)
for _ in range(n-1):
    a,b=map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs(v):


    for next_node in graph[v]:
        if visited[next_node]==0:
            visited[next_node]=v
            dfs(next_node)

dfs(1)
for i in range(2,len(visited)):
    print(visited[i])