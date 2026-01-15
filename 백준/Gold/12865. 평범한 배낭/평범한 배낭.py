import sys

n,k=map(int,sys.stdin.readline().split())
weight=[0]*(n+1)
value=[0]*(n+1)
dp=[[0]*(k+1) for _ in range(n+1)]
for i in range(1,n+1):
    weight[i],value[i]=map(int,sys.stdin.readline().split())

def memoization(i,j):
    if i<=0 or j<=0:
        return 0
    # memoization(있는 값 재사용)
    if dp[i][j]:
        return dp[i][j]
    if j<weight[i]:
        dp[i][j]=memoization(i-1,j)
    else:
        dp[i][j]=max(memoization(i-1,j-weight[i])+value[i],memoization(i-1,j))
    return dp[i][j]

print(memoization(n,k))