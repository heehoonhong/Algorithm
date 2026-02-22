import sys

input=sys.stdin.readline
n=int(input())
m=int(input())
INF=int(1e9)
graph=[[INF]*(n+1) for _ in range(n+1)]
for i in range(1,n+1):
    graph[i][i]=0
for _ in range(m):
    a,b,c=map(int,input().split())
    graph[a][b]=min(c,graph[a][b])

# k는 거쳐 가는 노드
for k in range(1,n+1):
    # i는 시작 노드
    for i in range(1,n+1):
        # j는 도착 노드
        for j in range(1,n+1):
            if graph[i][k]+graph[k][j]<graph[i][j]:
                graph[i][j]=graph[i][k]+graph[k][j]

for i in range(1,n+1):
    for j in range(1,n+1):
        if graph[i][j]==INF:
            print(0,end=' ')
        else:
            print(graph[i][j], end=' ')
    print()