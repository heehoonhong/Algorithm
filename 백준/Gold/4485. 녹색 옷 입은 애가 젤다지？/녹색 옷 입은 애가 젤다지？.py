import sys
import heapq

input=sys.stdin.readline
dx=[-1,1,0,0]
dy=[0,0,-1,1]
cnt=1
INF=int(1e9)
def dijkstra(graph,start,n):
    distances=[[INF]*n for _ in range(n)]
    x,y=start[0],start[1]
    distances[x][y]=graph[x][y]
    min_hq=[(graph[x][y],(x,y))]

    while min_hq:

        current_distance,current_node=heapq.heappop(min_hq)
        current_x,current_y=current_node[0],current_node[1]
        if current_distance>distances[current_x][current_y]:
            continue

        for i in range(4):
            nx=current_x+dx[i]
            ny=current_y+dy[i]
            if 0<=nx<n and 0<=ny<n :
                distance=current_distance+graph[nx][ny]
                if distance<distances[nx][ny]:
                    distances[nx][ny]=distance
                    heapq.heappush(min_hq,(distance,(nx,ny)))

    return distances

while True:
    n=int(input())
    if n==0: break
    graph=[[0]*n for _ in range(n)]
    for i in range(n):
        arr=list(map(int,input().split()))
        for j in range(n):
            graph[i][j]=arr[j]
    result=dijkstra(graph,(0,0),n)
    cc=str(cnt)
    print("Problem "+cc+":",result[-1][-1])
    cnt+=1