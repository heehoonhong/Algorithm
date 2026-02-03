import sys

input=sys.stdin.readline
n,m=map(int,input().split())
graph=[[] for _ in range(n)]
ans=0
v=[0]*n
for _ in range(m):
    a,b=map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)



def dfs(depth,now):
    global ans
    if depth==4:
        ans=1
        print(1)
        sys.exit()
        return

    for neighbor in graph[now]:
        if v[neighbor]==0:
            v[neighbor]=1
            dfs(depth+1,neighbor)
            v[neighbor]=0

for i in range(n):
    v[i]=1
    dfs(0,i)
    v[i]=0

print(0)