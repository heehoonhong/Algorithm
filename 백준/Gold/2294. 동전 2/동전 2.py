import sys

n,k=map(int,sys.stdin.readline().split())
coins=[]
for _ in range(n):
    coins.append(int(sys.stdin.readline()))
coins=list(set(coins))
coins.sort()
dp=[[10001]*(k+1) for _ in range(len(coins))]

for i in range(len(coins)):
    for j in range(k+1):
        dp[i][j]=dp[i-1][j]

    for j in range(coins[i],k+1):

        if j%coins[i]==0:
            dp[i][j]=min(dp[i][j],j//coins[i])
        else:
            dp[i][j]=min(dp[i][j],dp[i][j-coins[i]]+1)
    #print(coins[i], dp[i])
if dp[-1][-1]==10001:
    print(-1)
else:
    print(dp[-1][-1])

