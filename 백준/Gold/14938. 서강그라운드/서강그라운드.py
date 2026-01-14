import sys
import heapq

n,m,r=map(int,sys.stdin.readline().split())
items=list(map(int,sys.stdin.readline().split()))
graph=[[] for _ in range(n+1)]
for _ in range(r):
    a,b,l=map(int,sys.stdin.readline().split())
    graph[a].append((b,l))
    graph[b].append((a,l))

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
    result=dijkstra(graph,i)
    num=0
    for j in range(1,n+1):
        if result[j]<=m:
            num+=items[j-1]
    max_num=max(max_num,num)
print(max_num)