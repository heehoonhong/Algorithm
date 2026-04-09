from collections import deque

def solution(queue1, queue2):
    s1=sum(queue1)
    s2=sum(queue2)
    l=len(queue1)
    target=(s1+s2)//2
    q1=deque(queue1)
    q2=deque(queue2)
    # 누적합? 
    cnt=0
    while s1!=s2:
        if cnt==len(queue1)*3: break
        
        # q1의 합이 q2의 합보다 클 때
        if s1>s2:
            num=q1.popleft()
            s1-=num
            q2.append(num)
            s2+=num
            cnt+=1
        elif s2>s1:
            num=q2.popleft()
            s2-=num
            q1.append(num)
            s1+=num
            cnt+=1
    if s1!=s2: return -1
    else: return cnt
            
        
    
    
    