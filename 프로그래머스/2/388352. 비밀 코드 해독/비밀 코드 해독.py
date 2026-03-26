from itertools import combinations

def solution(n, q, ans):
    r=len(q[0])
    lst=list(range(1,n+1))
    result=0
    
    for element in combinations(lst,r):
        temp_ans=[]
        element=list(element)
        for i in range(len(q)):
            cnt=0
            for j in range(len(q[0])):
                if q[i][j] in element:
                    cnt+=1
            temp_ans.append(cnt)
        if temp_ans==ans: result+=1
    return result
            