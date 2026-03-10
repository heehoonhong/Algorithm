def solution(n, money):
    #money.sort()
    dp=[0]*(n+1)
    dp[0]=1
    for m in money:
        for j in range(m,n+1):
            dp[j]=dp[j]+dp[j-m]
            dp[j]=dp[j]%1000000007
    return dp[n]