import sys
from collections import deque

input=sys.stdin.readline
s,e=map(int,input().split())
visited=[-1]*100001
prev_node=[0]*100001
dx=[-1,1,2]

q=deque()
q.append(s)
visited[s]=0
cnt=0
while q:
    x=q.popleft()
    if x==e:
        cnt+=1
        break
    for i in range(2,-1,-1):
        if i==2:
            nx=x*2
        else:
            nx=x+dx[i]
        if 0<=nx<len(visited) and visited[nx]==-1:
            q.append(nx)
            visited[nx]=visited[x]+1
            prev_node[nx]=x
        #print(*q)
print(visited[e])
#print(cnt)
#print(*enumerate(prev_node))
curr=e
result=[]

while curr!=s:
    result.append(curr)
    curr=prev_node[curr]
result.append(curr)
result=result[::-1]
#result.append(e)
print(*result)
