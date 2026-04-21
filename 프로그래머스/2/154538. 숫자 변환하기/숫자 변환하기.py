from collections import deque

def solution(x, y, n):
    visited=[0]*(y+1)
    
    q=deque()
    q.append((x,0))
    visited[x]=1
    while q:
        num,cnt=q.popleft()
        for next_num in (num*2,num*3,num+n):
            if 0<=next_num<=y and visited[next_num]==0:
                q.append((next_num,cnt+1))
                visited[next_num]=visited[num]+1
        
    
    
    if visited[y]==0: return -1
    else: return visited[y]-1