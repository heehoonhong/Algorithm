import sys
from collections import deque

n=int(sys.stdin.readline())
k=int(sys.stdin.readline())
arr=[[0]*(n+1) for _ in range(n+1)]
directions=[(0,-1),(0,1),(-1,0),(1,0)]
snake=deque()
snake.append((1,1))
current_direction=(0,1)
change=dict()
def switch_direction(direction,LorR):
    if LorR=="L":
        if direction==(0,1):
            return (-1,0)
        elif direction==(1,0):
            return (0,1)
        elif direction==(0,-1):
            return (1,0)
        elif direction==(-1,0):
            return (0,-1)
    else:
        if direction==(0,1):
            return (1,0)
        elif direction==(1,0):
            return (0,-1)
        elif direction==(0,-1):
            return (-1,0)
        elif direction==(-1,0):
            return (0,1)
for _ in range(k):
    r,c=map(int,sys.stdin.readline().split())
    arr[r][c]=1

l=int(sys.stdin.readline())
for _ in range(l):
    x,c=sys.stdin.readline().split()
    x=int(x)
    change[x]=c

time=0
i=0
while True:
    time += 1
    nx,ny=snake[-1][0]+current_direction[0],snake[-1][1]+current_direction[1]

    # 벽
    if nx<1 or nx>n or ny<1 or ny>n:
        break
    # 자기 자신
    if (nx,ny) in snake:
        break

    # 시간이 바꾸는 시간대라면
    if time in change :
        nd1,nd2=switch_direction(current_direction,change[time])
        current_direction=(nd1,nd2)

    # 해당 칸에 사과가 있다면
    if arr[nx][ny] == 1:
        snake.append((nx,ny))
        # 사과 없어짐 처리
        arr[nx][ny]=0
    else:
        snake.popleft()
        snake.append((nx,ny))

print(time)