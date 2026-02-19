import sys
sys.setrecursionlimit(10**6)
def solution(begin, target, words):
    
    cnt=1000
    visited=[0]*len(words)
    def check_one(str1,str2):
        cc=0
        for i in range(len(str1)):
            if str1[i]!=str2[i]:
                cc+=1
        if cc==1:
            return True
        else:
            return False
    
    def dfs(current_cnt,current_word):
        nonlocal cnt
        if current_word==target:
            cnt=min(current_cnt,cnt)
            return
        for i in range(len(words)):
            flag=check_one(words[i],current_word)
            if flag and visited[i]==0:
                visited[i]=1
                dfs(current_cnt+1,words[i])
                visited[i]=0
    dfs(0,begin)
    if cnt==1000:
        return 0
    else:
        return cnt
