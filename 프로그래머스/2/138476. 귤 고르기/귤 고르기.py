from collections import defaultdict

def solution(k, tangerine):
    # k=6
    # 1:1, 2:2, 3:2, 4:1, 5:2
    # k=4
    # 1:1, 2:2, 3:2, 4:1, 5:2
    
    d=defaultdict(int)
    for t in tangerine:
        d[t]+=1
    
    d=list(d.items())
    d.sort(key=lambda x:(-x[1]))
    #print(d)
    
    cur=0
    cnt=0
    for (kk,v) in d:
        #print(kk,v)
        #print(cur)
        #print(cnt)
        #print("===")
        
        if cur+v<k:
            cnt+=1
            cur+=v
        
        else:
            cnt+=1
            cur=k
            break
    #print("=====")
    #print(cur)
    #print(cnt)
    return cnt