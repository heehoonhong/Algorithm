import sys

input=sys.stdin.readline
tc=int(input())
INF=int(1e9)
def bellman_ford(graph,start,n):
    distances=[0]*(n+1)
    distances[start]=0
    for _ in range(n-1):
        for current_node in range(1,n+1):
            
            for neighbor,weight in graph[current_node]:
                distance=distances[current_node]+weight
                if distance<distances[neighbor]:
                    distances[neighbor]=distance

    for current_node in range(1,n+1):

        for neighbor,weight in graph[current_node]:
            if distances[current_node]+weight<distances[neighbor]:
                return None
    return distances


for _ in range(tc):
    n,m,w=map(int,input().split())
    graph=[[] for _ in range(n+1)]
    for _ in range(m):
        s,e,t=map(int,input().split())
        graph[s].append((e,t))
        graph[e].append((s,t))
    for _ in range(w):
        s,e,t=map(int,input().split())
        graph[s].append((e,-t))
    result=bellman_ford(graph,1,n)
    if result is not None:
        print("NO")
    else:
        print("YES")