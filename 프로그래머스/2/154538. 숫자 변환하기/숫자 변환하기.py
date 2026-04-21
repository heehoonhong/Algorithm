from collections import deque

def solution(x, y, n):
    visited=[0]*(y+1)
    
    
    def bfs(num,prev_num):
        q=deque()
        q.append((num,prev_num))
        visited[num]=visited[prev_num]+1
        print(num)
        while q:
            num,prev=q.popleft()
            n1=num*2
            if 0<=n1<=y and (visited[n1]==0 ):
                q.append((n1,num))
                visited[n1]=visited[num]+1
                #print(n1)
            n1=num*3
            if 0<=n1<=y and (visited[n1]==0 ):
                q.append((n1,num))
                visited[n1]=visited[num]+1
                #print(n1)
            n1=num+n
            if 0<=n1<=y and (visited[n1]==0):
                q.append((n1,num))
                visited[n1]=visited[num]+1
                #print(n1)
            #print(visited)
    
    bfs(x,0)
    
    if visited[y]==0: return -1
    else: return visited[y]-1