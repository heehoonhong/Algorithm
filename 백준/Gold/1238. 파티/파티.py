import sys
import heapq

n,m,x=map(int,sys.stdin.readline().split())
graph=[[] for _ in range(n+1)]
for _ in range(m):
    s,e,w=map(int,sys.stdin.readline().split())
    graph[s].append((e,w))

def dijkstra(graph,start):
    distances={i:float('inf') for i in range(1,n+1)}
    distances[start]=0
    min_hq=[(0,start)]

    while min_hq:
        current_distance,current_node=heapq.heappop(min_hq)
        if current_distance>distances[current_node]:
            continue
        for neighbor,weight in graph[current_node]:
            distance=current_distance+weight
            if distance<distances[neighbor]:
                distances[neighbor]=distance
                heapq.heappush(min_hq,(distance,neighbor))
    return distances
max_num=0
for i in range(1,n+1):
    go=dijkstra(graph,i)[x]
    back=dijkstra(graph,x)[i]
    result=go+back
    max_num=max(max_num,result)
print(max_num)
