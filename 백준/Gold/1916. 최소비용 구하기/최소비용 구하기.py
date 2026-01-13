import sys
import heapq

n=int(sys.stdin.readline())
m=int(sys.stdin.readline())
graph=[[] for _ in range(n+1)]
for _ in range(m):
    s,e,w=map(int,sys.stdin.readline().split())
    graph[s].append((e,w))
start,end=map(int,sys.stdin.readline().split())

def dijkstra(graph,start):
    distances={i:float('inf') for i in range(1,n+1)}
    min_hq=[(0,start)]
    distances[start]=0

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

print(dijkstra(graph,start)[end])