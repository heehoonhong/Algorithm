import sys
from collections import deque

v,e=map(int,sys.stdin.readline().split())
graph=[[] for _ in range(v+1)]
indegree=[0]*(v+1)

for _ in range(e):
    edge=list(map(int,sys.stdin.readline().split()))
    for i in range(1,len(edge)-1):
        graph[edge[i]].append(edge[i+1])
        indegree[edge[i+1]]+=1

queue=deque()
result=[]
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

#print(*result)
if len(result)<v:
    print(0)
else:
    for element in result:
        print(element)