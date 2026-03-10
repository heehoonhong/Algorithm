def solution(n):
    # dp[i]: 가로 길이 i인 경우의 수
    dp=[0]*(n+1)
    dp[0]=1
    dp[2]=3
    dp[4]=11
    
    for i in range(6,n+1,2):
        for j in range(0,i-2,2):
            dp[i]+=(dp[j]*2)
        dp[i]+=(dp[i-2]*3)
        dp[i]=dp[i]%1000000007
            
        
        
    return dp[n]