def solution(msg):

    d={}
    for i in range(26):
        d[chr(ord("A")+i)]=i+1
    answer=[]
    base=""
    cnt=26
    for ch in msg:
        temp=base
        base=base+ch
        if base in d:
            continue
        else:
            cnt+=1
            d[base]=cnt
            
            answer.append(d[temp])
            
            base=ch
    answer.append(d[base])
    #print(base)
    #print(answer)
    return answer
            