import sys
import heapq

v,e=map(int,sys.stdin.readline().split())
graph=[[] for _ in range(v+1)]
indegree=[0]*(v+1)
min_hq=[]

for _ in range(e):
    a,b=map(int,sys.stdin.readline().split())
    graph[a].append(b)
    indegree[b]+=1

for i in range(1,v+1):
    if indegree[i]==0:
        heapq.heappush(min_hq,i)
result=[]
while min_hq:
    current=heapq.heappop(min_hq)
    result.append(current)

    for next_node in graph[current]:
        indegree[next_node]-=1
        if indegree[next_node]==0:
            heapq.heappush(min_hq,next_node)

print(*result)