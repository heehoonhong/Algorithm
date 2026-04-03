from collections import defaultdict

def solution(N, stages):
    per_stages=defaultdict(int)
    fail_rates={}
    for i in range(1,N+1):
        per_stages[i]=stages.count(i)
    #print(per_stages)
    total=len(stages)
    
    fail_rates[1]=per_stages[1]/total
    for i in range(2,N+1):
        total=total-per_stages[i-1]
        if total==0:
            fail_rates[i]=0
        else:
            fail_rates[i]=per_stages[i]/total
    answer=[]
    for k,v in fail_rates.items():
        answer.append((k,v))
    answer.sort(key=lambda x:(-x[1]))
    ans=[]
    for i in range(len(answer)):
        ans.append(answer[i][0])
    return ans
    