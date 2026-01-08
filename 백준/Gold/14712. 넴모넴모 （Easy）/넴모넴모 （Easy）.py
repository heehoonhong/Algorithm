import sys

n,m=map(int,sys.stdin.readline().split())
answer=0
grid=[[0]*(m+1) for _ in range(n+1)]

def dfs(depth):
    global answer
    if depth==n*m:
        answer+=1
        return
    x=depth//m+1
    y=depth%m+1

    if grid[x-1][y-1]==0 or grid[x-1][y]==0 or grid[x][y-1]==0:
        grid[x][y]=1
        dfs(depth+1)
        grid[x][y]=0
    dfs(depth+1)

dfs(0)
print(answer)