def solution(k, dungeons):
    # 해당 던전을 탐험하거나 안 하거나임
    # 일단 탐험을 하려면 dungeons[i][0] 보다 current_k가 커야 함
    # 큰 경우에도 그 던전을 탐험 안 할 수도 있음
    dl=len(dungeons)
    ans=0
    # depth, current_k, cnt(cnt는 탐험을 한 던전 개수)
    # cnt를 증가하냐 안 하냐에 따라 current_k가 달라짐
    
    def dfs(index,current_k,cnt,depth):
        nonlocal dl
        nonlocal ans
        
        
        visited[index]=1
        if current_k>=dungeons[index][0]:
            current_k-=dungeons[index][1]
            cnt+=1
        
        depth+=1
        
        if depth==dl:
            
            ans=max(ans,cnt)
            return
        
        for i in range(dl):
            if visited[i]==0:
                visited[i]=1
                dfs(i,current_k,cnt,depth)
                visited[i]=0
        
        
    
    visited=[0]*dl
    for i in range(dl):
        if visited[i]==0:
            visited[i]=1
            dfs(i,k,0,0)
            visited[i]=0
    return ans
    