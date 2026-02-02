import sys
from collections import deque

input=sys.stdin.readline
dist=0
shark=2
cnt=0
n=int(input())
fish=deque()
arr=[]
for _ in range(n):
    arr.append(list(map(int,input().split())))
for i in range(n):
    for j in range(n):
        if arr[i][j]==9:
            fish.append((i,j))
            arr[i][j]=0

def bfs(i,j):
    global shark,cnt,dist
    lst=[]
    v=[[0]*n for _ in range(n)]
    q=deque()
    q.append((i,j))
    while q:
        ci, cj = q.popleft()
        for di, dj in [(-1, 0), (1, 0), (0, 1), (0, -1)]:

            ni = ci + di
            nj = cj + dj
            # 이동 가능 조건
            if 0 <= ni < n and 0 <= nj < n and v[ni][nj] == 0 and shark >= arr[ni][nj]:
                q.append((ni, nj))
                v[ni][nj] = v[ci][cj]+1
                # 이동하는 동안에 물고기가 있다면 리스트에 저장하기
                if shark > arr[ni][nj] and arr[ni][nj]!=0:
                    lst.append((ni, nj,v[ni][nj]))

    # 리스트 정렬
    lst.sort(key=lambda x:(x[2],x[0],x[1]))
    return lst

while True:
    ci,cj= fish.popleft()

    lst=bfs(ci,cj)
    if not lst:
        break
    # bfs에서 정렬해야겠다
    ni,nj,distance=lst[0]
    #먹기 처리
    arr[ni][nj]=0
    cnt+=1
    if shark==cnt:
        shark+=1
        cnt=0
    dist+=distance
    fish.append((ni,nj))

print(dist)