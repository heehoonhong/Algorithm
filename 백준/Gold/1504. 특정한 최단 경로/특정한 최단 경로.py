import sys
import heapq

n,m=map(int,sys.stdin.readline().split())
graph=[[] for _ in range(n+1)]
for _ in range(m):
    s,e,w=map(int,sys.stdin.readline().split())
    graph[s].append((e,w))
    graph[e].append((s,w))
v1,v2=map(int,sys.stdin.readline().split())
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

start_1=dijkstra(graph,1)
start_v1=dijkstra(graph,v1)
start_v2=dijkstra(graph,v2)
v1_v2=start_1[v1]+start_v1[v2]+start_v2[n]
v2_v1=start_1[v2]+start_v2[v1]+start_v1[n]
result=min(v1_v2,v2_v1)
if result>=float('inf'):
    print(-1)
else:
    print(result)
