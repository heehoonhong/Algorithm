def solution(n,a,b):
    ans=0
    def dfs(arr,cnt):
        nonlocal ans
        new_arr=[]
        for i in range(0,len(arr),2):
            if (arr[i],arr[i+1])==(a,b) or (arr[i+1],arr[i])==(a,b):
                ans=cnt
                return
            elif arr[i] in (a,b):
                new_arr.append(arr[i])
            elif arr[i+1] in (a,b):
                new_arr.append(arr[i+1])
            else:
                new_arr.append(arr[i])
        dfs(new_arr,cnt+1)
                
            
    
    arr=list(range(1,n+1))
    dfs(arr,1)
    return ans