from collections import deque

def solution(priorities, location):
    answer = 0
    q=deque()
    for i in range(len(priorities)):
        q.append((i,priorities[i]))
    
    cnt=0
    while True:
        index,priority=q.popleft()
        flag=True
        for i in range(len(q)):
            if q[i][1]>priority:
                flag=False
        if index==location and flag:
            break
        
        if not flag:
            q.append((index,priority))
        else:
            cnt+=1
        
    return cnt+1