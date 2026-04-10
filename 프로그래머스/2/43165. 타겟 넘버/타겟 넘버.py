def solution(numbers, target):
    nl=len(numbers)
    cnt=0
    def dfs(depth, arr):
        nonlocal nl,target,cnt
        if depth==nl:
            s=sum(arr)
            if s==target:
                cnt+=1
            return
        
        dfs(depth+1,arr+[numbers[depth]])
        dfs(depth+1,arr+[-numbers[depth]])
    
    # depth, arr
    dfs(0,[0])
    return cnt