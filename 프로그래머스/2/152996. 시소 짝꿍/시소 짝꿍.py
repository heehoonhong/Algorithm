from collections import Counter

def solution(weights):
    cnt=0
    w=dict(Counter(weights))
    w=list(w.items())
    w.sort(key=lambda x:(x[0]))
    
    # 몸무게가 동일한 경우
    for i in range(len(w)):
        if w[i][1]>=2:
            cnt+=(w[i][1]*(w[i][1]-1)//2)
    
    # 몸무게가 다른 경우
    for i in range(len(w)):
        for j in range(i+1,len(w)):
            w1,w1_cnt=w[i][0],w[i][1]
            w2,w2_cnt=w[j][0],w[j][1]
            if w1*3==w2*2: 
                cnt+=(w1_cnt*w2_cnt)
            if w1*2==w2:
                cnt+=(w1_cnt*w2_cnt)
            if w1*4==w2*3:
                cnt+=(w1_cnt*w2_cnt)
    return cnt