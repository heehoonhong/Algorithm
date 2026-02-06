from collections import defaultdict

def solution(genres, plays):
    answer=[]
    d=defaultdict(list)
    
    dd=defaultdict(int)
    for i in range(len(genres)):
        d[genres[i]].append((plays[i],i))
        dd[genres[i]]+=plays[i]
    dd=list(dd.items())
    dd.sort(key=lambda x:-x[1])
    dd=dict(dd)
    
    for k in dd.keys():
        d[k].sort(key=lambda x:(-x[0],x[1]))
        for i in range(min(len(d[k]),2)):
            answer.append(d[k][i][1])
    return answer