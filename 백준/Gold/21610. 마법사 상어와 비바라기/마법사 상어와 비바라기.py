import sys

input=sys.stdin.readline
n,m=map(int,input().split())
dy=[0,-1,-1,0,1,1,1,0,-1]
dx=[0,0,-1,-1,-1,0,1,1,1]
graph=[[0]*n for _ in range(n)]
for i in range(n):
    line=list(map(int,input().split()))
    for j in range(n):
        graph[i][j]=line[j]

# clst1: 초기 구름 위치, clst2: 나중 구름 위치
clst1=[(n-1,0),(n-1,1),(n-2,0),(n-2,1)]

for _ in range(m):
    clst2 = []
    visited=[[0]*n for _ in range(n)]
    d,s=map(int,input().split())
    # 1. 구름이 d 방향으로 s칸 이동 및 2. 그 물의 양들이 1 증가
    for x,y in clst1:
        nx=(x+dx[d]*s)%n
        ny=(y+dy[d]*s)%n
        clst2.append((nx,ny))
        graph[nx][ny]+=1
        visited[nx][ny]=1

    # 3. 구름 사라짐
    # (4에서 2에서 증가한 칸들에 대해 물복사버그를 시행하므로 clst2는 놔둬야 함)
    clst1=[]

    for x,y in clst2:
        # 방향
        for  ddx,ddy in ((-1,-1),(-1,1),(1,-1),(1,1)):
            nx=x+ddx
            ny=y+ddy
            if 0<=nx<n and 0<=ny<n and graph[nx][ny]>0:
                graph[x][y]+=1

    # 5. 다시 맨 위에서 한 것처럼 이동을 위해
    # 물의 양이 2이상이고 clst2에 없는 것들에 대해서 clst1에 추가
    for i in range(n):
        for j in range(n):
            if graph[i][j] >=2 and visited[i][j]==0:
                graph[i][j]-=2
                clst1.append((i,j))


ans=0
for i in range(n):
    ans+=sum(graph[i])
print(ans)