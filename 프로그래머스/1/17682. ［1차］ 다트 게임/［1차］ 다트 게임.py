import re

def solution(dartResult):
    darts=re.findall('[0-9]+[SDT][#*]?',dartResult)
    answer=[]
    for i in range(len(darts)):
        num=int(re.findall('[0-9]+',darts[i])[0])
        for j in range(len(darts[i])):
            if darts[i][j]=='S':
                answer.append(num)
            elif darts[i][j]=='D':
                answer.append(num**2)
            elif darts[i][j]=='T':
                answer.append(num**3)
            elif darts[i][j]=='*':
                answer[-1]=2*answer[-1]
                if len(answer)>=2:
                    answer[-2]=answer[-2]*2
            elif darts[i][j]=='#':
                answer[-1]=-answer[-1]
    return sum(answer)
            
            