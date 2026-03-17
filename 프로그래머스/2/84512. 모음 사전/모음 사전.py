def solution(word):
    w=["A","E","I","O","U",""]
    ans=[]
    ss=1
    def dfs(depth,current_word):
        if depth==5:
            ans.append(current_word)
            return
        
        for i in range(6):
            dfs(depth+1,current_word+w[i])
    
    dfs(0,"")
    ans.sort()
    # sdf
    ans.pop(0)
    ans=list(set(ans))
    ans.sort()
    aa=0
    for i in range(len(ans)):
        if ans[i]==word:
            aa=i+1
    return aa