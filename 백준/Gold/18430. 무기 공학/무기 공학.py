import sys
from collections import deque

n,m=map(int,sys.stdin.readline().split())
grid=[[0]*(m+2) for _ in range(n+2)]
temp=[]
for _ in range(n):
    line=list(map(int,sys.stdin.readline().split()))
    temp.append(line)

for i in range(1,n+1):
    for j in range(1,m+1):
        grid[i][j]=temp[i-1][j-1]

max_weight=0
locations=deque()

def dfs(weight,depth):
    global locations
    global max_weight
    if depth==n*m:
        max_weight=max(max_weight,weight)
        return

    x=depth//m+1
    y=depth%m+1


    # 1번 모양
    if grid[x][y]>0 and grid[x][y+1]>0 and grid[x+1][y]>0:
        if (x,y) not in locations and (x,y+1) not in locations and (x+1,y) not in locations:
            # weight 추가 및 locations append
            weight+=2*grid[x][y]+grid[x][y+1]+grid[x+1][y]
            locations.append((x,y))
            locations.append((x, y+1))
            locations.append((x+1, y))
            dfs(weight,depth+1)
            weight-=2*grid[x][y]+grid[x][y+1]+grid[x+1][y]
            locations.pop()
            locations.pop()
            locations.pop()

    # 2번 모양
    if grid[x][y]>0 and grid[x-1][y]>0 and grid[x][y-1]>0:
        if (x,y) not in locations and (x-1,y) not in locations and (x,y-1) not in locations:
            weight += 2 * grid[x][y] + grid[x][y - 1] + grid[x - 1][y]
            locations.append((x, y))
            locations.append((x, y - 1))
            locations.append((x - 1, y))
            dfs(weight, depth + 1)
            weight -= 2 * grid[x][y] + grid[x][y - 1] + grid[x - 1][y]
            locations.pop()
            locations.pop()
            locations.pop()
    if grid[x][y]>0 and grid[x-1][y]>0 and grid[x][y+1]>0:
        if (x,y) not in locations and (x-1,y) not in locations and (x,y+1) not in locations:
            weight += 2 * grid[x][y] + grid[x][y + 1] + grid[x - 1][y]
            locations.append((x, y))
            locations.append((x, y + 1))
            locations.append((x - 1, y))
            dfs(weight, depth + 1)
            weight -= 2 * grid[x][y] + grid[x][y + 1] + grid[x - 1][y]
            locations.pop()
            locations.pop()
            locations.pop()

    if grid[x][y]>0 and grid[x+1][y]>0 and grid[x][y-1]>0:
        if (x,y) not in locations and (x+1,y) not in locations and (x,y-1) not in locations:
            weight += 2 * grid[x][y] + grid[x][y - 1] + grid[x + 1][y]
            locations.append((x, y))
            locations.append((x, y - 1))
            locations.append((x + 1, y))
            dfs(weight, depth + 1)
            weight -= 2 * grid[x][y] + grid[x][y - 1] + grid[x + 1][y]
            locations.pop()
            locations.pop()
            locations.pop()

    # 둘 다 안 될 때
    dfs(weight, depth + 1)


dfs(0,0)
if n<2 or m < 2:
    print(0)
else:
    print(max_weight)
