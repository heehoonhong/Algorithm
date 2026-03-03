import sys
from collections import deque

input=sys.stdin.readline
n=int(input())
dx=[-1,1,0,0]
dy=[0,0,-1,1]
ans=n*n
graph=[[0]*n for _ in range(n)]
visited=[[0]*n for _ in range(n)]
village_cnt=1
sx,sy,ex,ey=0,0,0,0

for i in range(n):
    line=list(map(int,input().split()))
    for j in range(n):
        graph[i][j]=line[j]

def bfs(x,y):
    global village_cnt
    q=deque()
    q.append((x,y))
    visited[x][y]=village_cnt


    while q:
        x,y=q.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<n and 0<=ny<n and visited[nx][ny]==0 and graph[nx][ny]==1:
                q.append((nx,ny))
                visited[nx][ny]=village_cnt

# bfs2의 방문 조건
# 하나를 제외하고 나머지는 바다여야 함(graph[nx][ny]==0)
# 그리고 육지인데 처음 bfs2 돌렸을 때의 번호랑 달라야 함
def bfs2(x,y):
    visited2 = [[0] * n for _ in range(n)]
    global ex,ey,sx,sy
    global ans
    # 초기의 마을 번호
    start=visited[x][y]
    sx,sy=x,y
    q=deque()
    q.append((x,y))
    visited2[x][y]=1

    while q:

        x,y=q.popleft()
        # 육지이고 처음 마을과 다른 마을이라면
        if graph[x][y]==1  and visited[x][y]!=start:
            #print(ans)
            ans=min(ans,visited2[x][y])

            ex,ey=x,y
            break
        for i in range(4):
            nx,ny=x+dx[i],y+dy[i]
            if 0<=nx<n and 0<=ny<n and visited2[nx][ny]==0:
                # 바다인 경우
                if graph[nx][ny]==0:
                    visited2[nx][ny]=visited2[x][y]+1
                    q.append((nx,ny))
                else:
                    if start!=visited[nx][ny]:
                        q.append((nx,ny))
                        visited2[nx][ny]=visited2[x][y]


for i in range(n):
    for j in range(n):
        if visited[i][j]==0 and graph[i][j]==1:
            bfs(i,j)
            village_cnt+=1

for i in range(n):
    for j in range(n):
        if visited[i][j]!=0:
            bfs2(i,j)

#print(sx,sy,ex,ey)
print(ans-1)