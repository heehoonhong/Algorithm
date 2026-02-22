import sys
from collections import deque

input=sys.stdin.readline
s,e=map(int,input().split())
visited=[-1]*100001
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
        if 0<=nx<len(visited) and (visited[nx]==-1 or visited[x]<visited[nx]):
            if i==2:
                q.appendleft(nx)
                visited[nx]=visited[x]
            else:
                q.append(nx)
                visited[nx]=visited[x]+1
        #print(*q)
print(visited[e])
#print(cnt)