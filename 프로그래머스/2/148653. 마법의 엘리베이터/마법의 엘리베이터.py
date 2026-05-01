def solution(storey):
    cnt=0
    num=storey
    while num>0:
        s=num%10
        num=num//10
        if s>5:
            cnt+=(10-s)
            num+=1
        elif s==5:
            if (num%10)+1>5:
                cnt+=(10-s)
                num+=1
            else:
                cnt+=s
                
        else:
            cnt+=s
    return cnt