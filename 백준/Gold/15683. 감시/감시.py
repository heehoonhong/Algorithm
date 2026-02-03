import sys
import copy

input=sys.stdin.readline
n,m=map(int,input().split())
arr=[]
cctv=[]
cnt=100
# 각각 인덱스별로 0,1,2,3 상,우,하,좌
dx=[-1,0,1,0]
dy=[0,1,0,-1]
for _ in range(n):
    arr.append(list(map(int,input().split())))
for i in range(n):
    for j in range(m):
        if arr[i][j]!=0 and arr[i][j]!=6:
            cctv.append((i,j))
        if arr[i][j]==0:
            cnt+=1
lc=len(cctv)

# index로 cctv 타입 매핑
cctv_types=[
    [],[1],[1,3],[0,1],[0,1,3],[0,1,2,3]
]

def calc(dlst):
    arr2 = copy.deepcopy(arr)
    for i in range(lc):
        rot=dlst[i] # 회전 방향 인덱스
        ci,cj=cctv[i][0],cctv[i][1]
        c_type=arr2[ci][cj]
        for dr in cctv_types[c_type]:
            dir=(dr+rot)%4
            di,dj=dx[dir],dy[dir]

            ni,nj=ci,cj
            while True:
                ni,nj=ni+di,nj+dj
                if 0<=ni<n and 0<=nj<m:
                    if arr2[ni][nj]==6:
                        break
                    elif arr2[ni][nj]==0:
                        arr2[ni][nj]=7
                # 범위가 아닐 때
                else:
                    break
    cc=0
    for i in range(n):
        for j in range(m):
            if arr2[i][j]==0:
                cc+=1
    return cc
# dlst: depth에 해당하는 cctv의 회전 방향
def dfs(depth,dlst):
    global cnt
    if depth==lc:

        cnt=min(calc(dlst),cnt)
        #print(cnt)
        return

    # 0도 회전
    dfs(depth+1,dlst+[0])
    # 90도 회전
    dfs(depth+1,dlst+[1])
    # 180도 회전
    dfs(depth+1,dlst+[2])
    # 270도 회전
    dfs(depth+1,dlst+[3])

# 두 번째 파라미터는 depth에 대한 cctv의 회전 방향임
dfs(0,[])
print(cnt)