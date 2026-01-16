import sys

n,m=map(int,sys.stdin.readline().split())
memory=[0]+list(map(int,sys.stdin.readline().split()))
cost=[0]+list(map(int,sys.stdin.readline().split()))
total_cost=sum(cost)
dp=[[0]*(total_cost+1) for _ in range(n+1)]
#print(memory)
#print(cost)
for i in range(1,n+1):
    # 이전 줄의 dp 결과들을 지금 dp 행에 가져옴
    #for j in range(1,total_cost+1):
    #    dp[i][j]=dp[i-1][j]

    for j in range(total_cost+1):
        dp[i][j]=dp[i-1][j]
        if j >= cost[i]:
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - cost[i]] + memory[i])
    #print(dp[i])

result=0

for j in range(total_cost+1):
    if dp[n][j]>=m:
        result=j
        break
print(result)


