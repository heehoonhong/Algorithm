import sys

input=sys.stdin.readline
r,c=map(int,input().split())
v = [0] * 128
ans=1
arr=[['0']*c for _ in range(r)]
for i in range(r):
    s=input().strip()
    for j in range(c):
        arr[i][j]=s[j]

def dfs(ci,cj,cc):
    global ans
    ans=max(cc,ans)

    # 네 방향, 범위 내, visited x
    for di,dj in ((-1,0),(1,0),(0,-1),(0,1)):
        ni,nj=ci+di,cj+dj
        if 0<=ni<r and 0<=nj<c and v[ord(arr[ni][nj])]==0:
            v[ord(arr[ni][nj])]=1
            dfs(ni,nj,cc+1)
            v[ord(arr[ni][nj])]=0

v[ord(arr[0][0])]=1
dfs(0,0,1)
print(ans)