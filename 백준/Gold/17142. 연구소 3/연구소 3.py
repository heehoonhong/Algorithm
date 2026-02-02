import sys
from collections import deque

input=sys.stdin.readline
virus=[]
cnt=0
n,m=map(int,input().split())
arr=[]
for _ in range(n):
    arr.append(list(map(int,input().split())))
for i in range(n):
    for j in range(n):
        if arr[i][j]==2:
            virus.append((i,j))
        if arr[i][j]==0:
            cnt+=1

lv=len(virus)
def bfs(vlst):
    v=[[0]*n for _ in range(n)]
    q=deque()

    for vi,vj in vlst:
        q.append((vi,vj))
        v[vi][vj]=1

    global cnt
    # cnt 값 복사
    CNT=cnt

    while q:
        ci, cj = q.popleft()
        for di, dj in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            ni, nj = ci + di, cj + dj
            if 0 <= ni < n and 0 <= nj < n and v[ni][nj] == 0 and arr[ni][nj] != 1:
                q.append((ni, nj))
                v[ni][nj] = v[ci][cj] + 1
                if arr[ni][nj]==0:
                    CNT -= 1
                    # 빈 칸이 전부 사라졌을 때
                    if CNT == 0:
                        return v[ni][nj]-1

    return n*n

def dfs(depth,start,vlst):
    global ans
    if depth==m:
        ans=min(ans,bfs(vlst))

        return
    for i in range(start,lv):
        dfs(depth+1,i+1,vlst+[virus[i]])

ans=n*n

dfs(0,0,[])
if ans==n*n:
    if cnt==0:
        print(0)
    else:
        print(-1)
else:
    print(ans)

