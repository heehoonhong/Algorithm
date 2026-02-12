def solution(numbers, target):
    ln=len(numbers)
    cnt=0
    def dfs(depth,total):
        nonlocal cnt
        if depth==ln:
            if total==target:
                cnt+=1
            return
        
        dfs(depth+1,total+numbers[depth])
        dfs(depth+1,total-numbers[depth])
    
    dfs(0,0)
    return cnt
            