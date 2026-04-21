from collections import Counter
from collections import defaultdict

def solution(topping):
    answer=0
    a1=defaultdict(int)
    a2=dict(Counter(topping))
    for i in range(len(topping)):
        if len(a1.keys())==len(a2.keys()):answer+=1
        #print(a1)
        #print(a2)
        #print("=====")
        topp=topping[i]
        if a2[topp]>0:
            a2[topp]-=1
            a1[topp]+=1
        # value가 0인 것도 key로서 남아있기 때문에 삭제해줘야 함.
        if a2[topp]==0:
            del(a2[topp])
        
        
    return answer
    