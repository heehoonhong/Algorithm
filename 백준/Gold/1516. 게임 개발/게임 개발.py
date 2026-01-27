import sys
from collections import deque

v=int(sys.stdin.readline())
graph=[[] for _ in range(v+1)]
indegree=[0]*(v+1)
# dp i번째 노드까지 걸리는데 드는 최소 시간
dp=[0]*(v+1)
times=[0]*(v+1)
result=[]
for i in range(1,v+1):
    line=list(map(int,sys.stdin.readline().split()))
    times[i]=line[0]

    # 나중에 들어온 건물들 사이의 관계는 없고,
    # 그냥 현재 건물보다 먼저 건물들이 지어져야 한다는 거임.
    for prev in line[1:-1]:
        graph[prev].append(i)
        indegree[i]+=1

#print(graph)
queue=deque()
for i in range(1,v+1):
    # indegree가 0인 것부터 queue에 append
    if indegree[i]==0:
        queue.append(i)
        dp[i]=times[i]

while queue:
    # pop해서 result에 추가
    current=queue.popleft()
    result.append(current)

    for next_node in graph[current]:
        indegree[next_node]-=1
        dp[next_node] = max(dp[next_node], dp[current] + times[next_node])

        if indegree[next_node]==0:
            queue.append(next_node)

for i in range(1,v+1):
    print(dp[i])