def solution(record):
    d={}
    answer=[]
    for r in record:
        l=r.split()
        state,uid=l[0],l[1]
        if state=='Enter':
            answer.append((uid,state))
            d[uid]=l[2]
            
        elif state=='Leave':
            answer.append((uid,state))
            
        else:
            d[uid]=l[2]
    result=[]
    for (uid,state) in answer:
        if state=='Enter':
            result.append((d[uid]+"님이 들어왔습니다."))
        else:
            result.append((d[uid]+"님이 나갔습니다."))
    return result