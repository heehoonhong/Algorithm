def solution(triangle):
    dp=[]
    n=len(triangle)
    for i in range(n):
        dp.append([0]*(i+1))
    for i in range(n):
        for j in range(i+1):
            if j==0:
                dp[i][j]=dp[i-1][j]+triangle[i][j]
            elif i==j:
                dp[i][j]=dp[i-1][j-1]+triangle[i][j]
            else:
                dp[i][j]=max(dp[i-1][j-1],dp[i-1][j])+triangle[i][j]
    
    result=max(dp[n-1])
    return result