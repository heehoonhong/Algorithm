from collections import deque
import sys

v,e=map(int,sys.stdin.readline().split())
graph=[[] for _ in range(v+1)]
indegree=[0]*(v+1)
edges=[]

for _ in range(e):
    start,end=map(int,sys.stdin.readline().split())
    edges.append((start,end))

for edge in edges:
    graph[edge[0]].append(edge[1])
    indegree[edge[1]]+=1
result=[]
def topology_sort():
    queue=deque()

    for i in range(1,v+1):
        if indegree[i]==0:
            queue.append(i)

    while queue:
        current=queue.popleft()
        result.append(current)

        for next_node in graph[current]:
            indegree[next_node]-=1
            if indegree[next_node]==0:
                queue.append(next_node)
topology_sort()
print(*result)