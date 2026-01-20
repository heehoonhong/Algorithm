import sys

n=int(sys.stdin.readline())
grid=[]
for _ in range(n):
    grid.append(list(map(int,sys.stdin.readline().split())))
dp=[[[-1]*3 for _ in range(n)] for _ in range(n)]

def dfs(x,y,direction):
    if x==n-1 and y==n-1:
        return 1
    if dp[x][y][direction]!=-1:
        return dp[x][y][direction]

    dp[x][y][direction]=0
    # direction 0,1,2 각각 가로,대각선, 세로
    if direction==0:
        if 0<=(x+1)<n and 0<=(y+1)<n and grid[x+1][y+1]==0 and grid[x][y+1]==0 and grid[x+1][y]==0:
            dp[x][y][direction]+=dfs(x+1,y+1,1)
        if 0<=(y+1)<n and grid[x][y+1]==0:
            dp[x][y][direction]+=dfs(x,y+1,0)
    if direction==1:
        # 대각선
        if 0<=(x+1)<n and 0<=(y+1)<n and grid[x+1][y+1]==0 and grid[x][y+1]==0 and grid[x+1][y]==0:
            dp[x][y][direction] += dfs(x + 1, y + 1, 1)
        # 가로
        if 0<=(y+1)<n and grid[x][y+1]==0:
            dp[x][y][direction]+=dfs(x,y+1,0)
        # 세로
        if 0<=(x+1)<n and grid[x+1][y]==0:
            dp[x][y][direction]+=dfs(x+1,y,2)
    if direction==2:
        # 세로
        if 0 <= (x + 1) < n and grid[x + 1][y] == 0:
            dp[x][y][direction] += dfs(x + 1, y, 2)
        # 대각선
        if 0 <= (x + 1) < n and 0 <= (y + 1) < n and grid[x + 1][y + 1] == 0 and grid[x][y + 1] == 0 and grid[x + 1][y] == 0:
            dp[x][y][direction] += dfs(x + 1, y + 1, 1)
    return dp[x][y][direction]

print(dfs(0,1,0))