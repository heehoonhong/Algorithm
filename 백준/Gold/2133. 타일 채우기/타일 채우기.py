import sys

n=int(sys.stdin.readline())
dp=[0]*31
dp[0]=1
dp[2]=3
for i in range(4,n+1,2):
    dp[i]+=3*dp[i-2]
    for j in range(i-4,-1,-2):
        dp[i]+=2*dp[j]
print(dp[n])