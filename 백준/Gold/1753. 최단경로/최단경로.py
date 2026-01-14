import sys
import heapq

v,e=map(int,sys.stdin.readline().split())
start=int(sys.stdin.readline())
graph=[[] for _ in range(v+1)]
for _ in range(e):
    a,b,c=map(int,sys.stdin.readline().split())
    graph[a].append((b,c))
def dijkstra(graph,start):
    distances={i:float('inf') for i in range(1,v+1)}
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

result=dijkstra(graph,start)
for i in range(1,len(result)+1):
    if result[i]==float('inf'):
        print("INF")
    else:
        print(result[i])