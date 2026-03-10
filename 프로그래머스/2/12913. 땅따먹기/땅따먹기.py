def solution(land):
    n=len(land)
    dp=[[0]*4 for _ in range(n)]
    
    for i in range(4):
        dp[0][i]=land[0][i]
    
    for i in range(1,n):
        for j in range(4):
            ans=0
            for k in range(4):
                if k!=j and ans<dp[i-1][k]:
                    ans=dp[i-1][k]
            dp[i][j]=ans+land[i][j]
            #print(dp[i][j],end=' ')
        #print()
    
    ans=0
    for i in range(4):
        if ans<dp[n-1][i]:
            ans=dp[n-1][i]
    return ans
            