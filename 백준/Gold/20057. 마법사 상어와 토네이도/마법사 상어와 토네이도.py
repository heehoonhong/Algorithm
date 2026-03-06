import sys

input=sys.stdin.readline
dx=[0,1,0,-1]
dy=[-1,0,1,0]
n=int(input())
x,y=n//2,n//2
dr=0
graph=[]
cur=0
cur_mx=1
flag=0

mul=[2,10,7,1,5,10,7,1,2,0]
ax=[[-2,-1,-1,-1,0,1,1,1,2,0],
    [0,1,0,-1,2,1,0,-1,0,1],
    [2,1,1,1,0,-1,-1,-1,-2,0],
    [0,-1,0,1,-2,-1,0,1,0,-1]]
ay=[[0,-1,0,1,-2,-1,0,1,0,-1],
    [-2,-1,-1,-1,0,1,1,1,2,0],
    [0,1,0,-1,2,1,0,-1,0,1],
    [2,1,1,1,0,-1,-1,-1,-2,0]]


for _ in range(n):
    line=list(map(int,input().split()))
    graph.append(line)
ans=0
while (x,y)!=(0,0):

    # 다음 좌표로 이동
    x = x + dx[dr]
    y = y + dy[dr]

    if graph[x][y]>0:
        total=0
        for i in range(10):
            nx=x+ax[dr][i]
            ny=y+ay[dr][i]
            val=(mul[i]*graph[x][y])//100
            if 0<=nx<n and 0<=ny<n:
                if i==9:
                    graph[nx][ny]+=(graph[x][y]-total)
                else:
                    graph[nx][ny]+=val
                    total+=val
            else:
                if i==9:
                    ans+=(graph[x][y]-total)
                else:
                    ans+=val
                    total+=val

        graph[x][y]=0

    # cur은 현재 방향에서 몇 번 갔는지를 알려줌
    cur+=1

    if cur==cur_mx:
        cur = 0
        dr = (dr + 1) % 4
        if flag==0:
            flag=1
        else:
            flag=0
            cur_mx+=1

print(ans)