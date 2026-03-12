def solution(board):
    col,row=len(board),len(board[0])
    dp=[[0]*row for _ in range(col) ]
    result=0
    # dp[i][j]: i부터 j까지의 최대 행 개수
    for i in range(col):
        for j in range(row):
            if i==0 or j==0:
                if board[i][j]==1:
                    dp[i][j]=1
            else:
                
                res=min(min(dp[i-1][j],dp[i-1][j-1]),dp[i][j-1])
                if board[i][j]==1:
                    dp[i][j]=res+1
            result=max(dp[i][j],result)
            #print(dp[i][j],end=' ')
        #print()
    return result*result    
            
    