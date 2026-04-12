from collections import deque

def solution(people, limit):
    people.sort(reverse=True)
    s=0
    e=len(people)-1
    q=deque(people)
    cnt=0
    
    while len(q)>1:
        if q[0]+q[-1]<=limit:
            cnt+=1
            q.popleft()
            q.pop()
        else:
            q.popleft()
            cnt+=1
    if len(q)==1:
        cnt+=1
        q.pop()
    return cnt
        
    
        