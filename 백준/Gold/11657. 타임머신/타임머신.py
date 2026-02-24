import sys

input=sys.stdin.readline
n,m=map(int,input().split())
graph=[[] for _ in range(n+1)]
def bellman_ford(graph,start,n):
    distances=[float('inf')]*(n+1)
    distances[start]=0

    for _ in range(n-1):
        for current_node in range(1,n+1):
            if distances[current_node]==float('inf'):
                continue
            for neighbor,weight in graph[current_node]:
                distance=distances[current_node]+weight
                if distance<distances[neighbor]:
                    distances[neighbor]=distance

    for current_node in range(1,n+1):
        if distances[current_node]==float('inf'):
            continue
        for neighbor,weight in graph[current_node]:
            # 이웃에 도달을 못할 때
            if distances[current_node]+weight<distances[neighbor]:
                return None
    return distances

for _ in range(m):
    a,b,c=map(int,input().split())
    graph[a].append((b,c))
result=bellman_ford(graph,1,n)
if result is None:
    print(-1)
else:
    for i in range(2,n+1):
        if result[i]==float('inf'):
            print(-1)
        else:
            print(result[i])