import sys

input=sys.stdin.readline
sys.setrecursionlimit(10**6)
n=int(input())
graph=[[] for _ in range(n+1)]
visited=[0]*(n+1)
max_node=0
max_dist=0
for _ in range(n):
    arr=list(map(int,input().split()))
    a=arr[0]
    for i in range(1,len(arr)-1,2):
        b,w=arr[i],arr[i+1]
        graph[a].append((b,w))
        graph[b].append((a,w))
def dfs(node,dist):
    global max_dist,max_node
    if visited[node]==0:
        visited[node]=1
    if dist>max_dist:
        max_dist=dist
        max_node=node

    for next_node,next_dist in graph[node]:
        if visited[next_node]==0:
            dfs(next_node,dist+next_dist)

dfs(1,0)
visited=[0]*(n+1)
dfs(max_node,0)
print(max_dist)