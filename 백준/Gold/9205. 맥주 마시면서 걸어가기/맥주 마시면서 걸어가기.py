import sys
from collections import deque

def bfs():
    q=deque()
    q.append((home_x,home_y))
    while q:
        x,y=q.popleft()
        dis=abs(festival_x-x)+abs(festival_y-y)
        if dis<=1000:
            print("happy")
            return
        for i in range(n):
            if visited[i]==0:
                xx,yy=graph[i]
                if abs(xx-x)+abs(yy-y)<=1000:
                    q.append((xx,yy))
                    visited[i]=1
    print("sad")
    return


tc=int(input())
input=sys.stdin.readline
for _ in range(tc):
    n=int(input())
    home_x,home_y=map(int,input().split())
    graph=[]
    for _ in range(n):
        x,y=map(int,input().split())
        graph.append((x,y))
    festival_x,festival_y=map(int,input().split())
    visited=[0]*(n+1)
    bfs()