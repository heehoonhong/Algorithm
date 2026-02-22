import sys
from collections import deque

input=sys.stdin.readline
s,e=map(int,input().split())
visited=[0]*100001
dx=[-1,1,2]

q=deque()
q.append(s)
cnt=0
while q:
    x=q.popleft()
    if x==e:
        cnt+=1
        continue
    for i in range(3):
        if i==2:
            nx=x*2
        else:
            nx=x+dx[i]
        if 0<=nx<len(visited) and (visited[nx]==0 or visited[nx]==visited[x]+1):
            visited[nx]=visited[x]+1
            q.append(nx)
print(visited[e])
print(cnt)