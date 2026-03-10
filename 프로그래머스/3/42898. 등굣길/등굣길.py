def solution(m, n, puddles):
    # dp[i][j] (i,j) 까지 갈 수 있는 경우의 수
    dp=[[0]*(m+1) for _ in range(n+1)]
    dp[1][1]=1
    for i in range(len(puddles)):
        dp[puddles[i][1]][puddles[i][0]]=-1
    
    for i in range(1,n+1):
        for j in range(1,m+1):
            if i==1 and j==1:
                dp[i][j]=1
                dp[i][j]=dp[i][j]%1000000007
                continue
            
            if dp[i][j]!=-1:
                dp[i][j]=dp[i-1][j]+dp[i][j-1]
                dp[i][j]=dp[i][j]%1000000007
            else:
                dp[i][j]=0
            
            #print(dp[i][j],end=' ')
        #print()
    return dp[n][m]
                
            
            