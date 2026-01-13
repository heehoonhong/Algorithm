import sys
import heapq

n,e=map(int,sys.stdin.readline().split())
graph=[[] for _ in range(n+1)]
for _ in range(e):
    a,b,c=map(int,sys.stdin.readline().split())
    graph[a].append((b,c))
    graph[b].append((a,c))
v1,v2=map(int,sys.stdin.readline().split())
visited=[0]*(n+1)

def dijkstra(graph,start):
    distances={i:float('inf') for i in range(1,n+1)}
    distances[start]=0
    min_hq=[(0,start)]

    while min_hq:
        current_distance,current_node=heapq.heappop(min_hq)
        if current_distance>distances[current_node]:
            continue
        for neighbor,weight in graph[current_node]:
            distance=weight+current_distance
            if distance<distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(min_hq, (distance, neighbor))
    return distances

dist_from_1=dijkstra(graph,1)
dist_from_v1=dijkstra(graph,v1)
dist_from_v2=dijkstra(graph,v2)

path_v1_first=dist_from_1[v1]+dist_from_v1[v2]+dist_from_v2[n]
path_v2_first=dist_from_1[v2]+dist_from_v2[v1]+dist_from_v1[n]
result=min(path_v1_first,path_v2_first)
if result>=float('inf'):
    print(-1)
else:
    print(result)