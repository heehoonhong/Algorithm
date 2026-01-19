import sys

n,m=map(int,sys.stdin.readline().split())
sys.setrecursionlimit(10**6)
grid=[]
dx=[-1,1,0,0]
dy=[0,0,-1,1]
for _ in range(n):
    grid.append(list(map(int,sys.stdin.readline().split())))
dp=[[-1]*m for _ in range(n)]
# dp[x][y]: x,y 에서 도착 지점까지의 갈 수 있는 경로의 개수


def dfs(x,y):
    if x==n-1 and y==m-1:
        return 1
    if dp[x][y]!=-1:
        return dp[x][y]

    # 일단 방문 처리
    dp[x][y]=0
    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]
        if 0<=nx<n and 0<=ny<m:
            if grid[x][y]>grid[nx][ny]:
                dp[x][y]+=dfs(nx,ny)
    return dp[x][y]

print(dfs(0,0))