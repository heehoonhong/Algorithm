def solution(k, ranges):
    x=0
    ls=[]
    answer=[]
    while k>1:
        ls.append((x,k))
        if k%2==0:
            k=k//2
        else:
            k=k*3+1
        x+=1
    ls.append((x,k))
    
    def calc(a,b,ls):
        b=b+len(ls)-1
        if a>b: return -1
        result=0
        for i in range(a,b):
            result+=((ls[i][1]+ls[i+1][1])/2)
            #print(result)
        return result
    for i in range(len(ranges)):
        x,y=ranges[i][0],ranges[i][1]
        answer.append(calc(x,y,ls))
    return answer
        