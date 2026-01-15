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
    distances[start]=0
    min_hq=[(0,start)]
    prev_node=[0]*(n+1)
    while min_hq:
        current_distance,current_node=heapq.heappop(min_hq)
        if current_distance>distances[current_node]:
            continue
        for neighbor,weight in graph[current_node]:
            distance=current_distance+weight
            if distance<distances[neighbor]:
                distances[neighbor]=distance
                prev_node[neighbor]=current_node
                heapq.heappush(min_hq,(distance,neighbor))
    return distances,prev_node

dis,prev=dijkstra(graph,start)
path=[]
cur=end
path.append(cur)
while cur!=start:
    cur=prev[cur]
    path.append(cur)
path=path[::-1]
print(dis[end])
print(len(path))
print(*path)
#print(prev)


