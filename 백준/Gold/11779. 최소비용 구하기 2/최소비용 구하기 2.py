import sys
import heapq

n=int(sys.stdin.readline())
m=int(sys.stdin.readline())
graph=[[] for _ in range(n+1)]
for _ in range(m):
    s,e,w=map(int,sys.stdin.readline().split())
    graph[s].append((e,w))
start,end=map(int,sys.stdin.readline().split())
q=[]
def dijkstra(graph,start):
    distances={i:float('inf') for i in range(n+1)}
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
                prev_node[neighbor]=current_node
                distances[neighbor]=distance
                heapq.heappush(min_hq,(distance,neighbor))
    return distances,prev_node

result,prev_map=dijkstra(graph,start)

path=[]

curr=end
path.append(end)
while curr!=start:
    curr=prev_map[curr]
    path.append(curr)
print(result[end])
print(len(path))
path.reverse()

print(*path)
