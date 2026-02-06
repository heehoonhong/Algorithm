def solution(clothes):
    d={}
    for i in range(len(clothes)):
        d[clothes[i][1]]=d.get(clothes[i][1],0)+1
    
    answer=1
    for v in d.values():
        answer*=(v+1)
    return answer-1

