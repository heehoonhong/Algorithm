import sys

input=sys.stdin.readline
n=int(input())
a=list(map(int,input().split()))
visited=[0]*n
ans=0
def dfs(depth,arr):
    global ans
    if depth==n:
        total=0
        for i in range(n-1):
            total+=abs(arr[i]-arr[i+1])
        ans=max(ans,total)
        return

    for i in range(n):
        if visited[i]==0:
            visited[i]=1
            dfs(depth+1,arr+[a[i]])
            visited[i]=0


for i in range(n):
    if visited[i]==0:
        visited[i]=1
        dfs(1,[]+[a[i]])
        visited[i]=0
print(ans)