import sys


sys.setrecursionlimit(10**6)
def solution(info, n, m):
    # 물건 i에 대해서, ss
    # A도둑이면 info[i][0] 흔적 남기고,
    # B도둑이면 info[i][1] 흔적 남김
    # A 도둑은 흔적 누적 개수가 n개 미만이어야 하고
    # B 도둑은 흔적 누적 개수가 m개 미만이어야 함.
    il=len(info)
    ans=n
    def dfs(depth,current_a,current_b):
        nonlocal il
        nonlocal ans
        if current_a>=n: return
        if current_b>=m: return
        
        if depth==il:
            ans=min(ans,current_a)
            return
        
        # a도둑이 훔치는 경우
        dfs(depth+1,current_a+info[depth][0],current_b)
        # b도둑이 훔치는 경우
        dfs(depth+1,current_a,current_b+info[depth][1])
    
    
    # dfs로는 무조건 시간 초과날 줄 알고 있긴 했음
    # 그리디?
    # 그리디도 아님 왜냐하면 b먼저 큰 것들을 담는 경우보다
    # 더 효율적인 게 있을 수 있음
    # 따라서 냅색(dp)문제임... 어렵구만
    
    dp=[[float('inf')]*m for _ in range(len(info)+1)]
    
    # dp[i][j]: i번째 물건을 훔칠 때, b도둑이 j만큼 훔쳤을 때 a도둑이 최소로 훔치는 값
    dp[0][0]=0
    
    for i in range(1,len(info)+1):
        trace_a,trace_b=info[i-1]
        for j in range(m):
            if dp[i-1][j]!=float('inf'):
                
                # a도둑이 훔칠 때
                dp[i][j]=min(dp[i][j],dp[i-1][j]+trace_a)
                
                # b도둑이 훔칠 때(dp의 값은 애초에 a도둑의 값이므로 여기에는 j값만 변함)
                if j+trace_b<m:
                    dp[i][j+trace_b]=min(dp[i-1][j],dp[i][j+trace_b])
    
    answer=float('inf')
    s=len(info)
    for i in range(m):
        if dp[s][i]<n:
            answer=min(answer,dp[s][i])
    if answer==float('inf'):return -1
    else: return answer
    
    