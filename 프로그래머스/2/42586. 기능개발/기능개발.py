from collections import deque

def solution(progresses, speeds):
    result=[]
    days_left=deque()
    for i in range(len(speeds)):
        if (100-progresses[i])%speeds[i]==0:
            days_left.append((100-progresses[i])//speeds[i])
        else:
            days_left.append((100-progresses[i])//speeds[i]+1)
    while days_left:
        cnt=0
        current_day=days_left.popleft()
        cnt+=1
        while len(days_left)>0 and current_day>=days_left[0]:
            cnt+=1
            days_left.popleft()
        result.append(cnt)
    return result      