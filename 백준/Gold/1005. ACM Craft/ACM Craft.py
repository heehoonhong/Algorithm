import sys
from collections import deque

t=int(sys.stdin.readline())
for _ in range(t):
    v,e=map(int,sys.stdin.readline().split())
    graph=[[] for _ in range(v+1)]
    dp=[0]*(v+1)
    indegree=[0]*(v+1)
    times=[0]+list(map(int,sys.stdin.readline().split()))
    for _ in range(e):
        start,end=map(int,sys.stdin.readline().split())
        graph[start].append(end)
        indegree[end]+=1
    target=int(sys.stdin.readline())

    result=[]
    queue=deque()

    for i in range(1,v+1):
        if indegree[i]==0:
            queue.append(i)
            dp[i]=times[i]
    while queue:
        current=queue.popleft()
        result.append(current)

        for next_node in graph[current]:
            dp[next_node]=max(dp[next_node],dp[current]+times[next_node])
            indegree[next_node]-=1
            if indegree[next_node]==0:
                queue.append(next_node)
    print(dp[target])