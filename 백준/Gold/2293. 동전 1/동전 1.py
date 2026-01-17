import sys

n,k=map(int,sys.stdin.readline().split())
coins=[]
dp=[0]*(k+1)
dp[0]=1
# dp[i]: i원을 만들 수 있는 경우의 수
for _ in range(n):
    coins.append(int(sys.stdin.readline()))

for coin in coins:
    for j in range(coin,k+1):
            dp[j]=dp[j]+dp[j-coin]

print(dp[k])
