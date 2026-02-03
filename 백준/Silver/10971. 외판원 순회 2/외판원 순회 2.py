import sys

input=sys.stdin.readline
n=int(input())
arr=[]
ans=10000000
for _ in range(n):
    arr.append(list(map(int,input().split())))
v=[0]*n
def dfs(depth,now,cost):
    global ans

    if cost>=ans:
        return


    if depth==n-1:
        if arr[now][0]==0:
            return
        else:
            ans=min(ans,cost+arr[now][0])

        return

    for i in range(n):
        if v[i]==0 and arr[now][i]!=0:
            v[i]=1
            # 여기에서 i는 다음 이동 마을
            dfs(depth+1,i,cost+arr[now][i])
            v[i]=0
v[0]=1
dfs(0,0,0)

print(ans)