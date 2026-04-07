def solution(dr):
    num=""
    temp=0
    answer=[]
    for i in range(len(dr)):
        if dr[i].isdigit() and not dr[i-1].isdigit():
            if dr[i+1].isdigit():
                temp=int(dr[i:i+2])
                i+=1
            else:
                temp=int(dr[i])
        elif dr[i]=='S':
            answer.append(temp)
        elif dr[i]=='D':
            answer.append(temp**2)
        elif dr[i]=='T':
            answer.append(temp**3)
        elif dr[i]=='#':
            answer[-1]= -answer[-1]
        elif dr[i]=='*':
            answer[-1]=answer[-1]*2
            if len(answer)>=2:
                answer[-2]=2*answer[-2]
    #print(answer)
    return sum(answer)