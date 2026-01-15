import sys

n,k=map(int,sys.stdin.readline().split())
weight=[0]*(n+1)
value=[0]*(n+1)
dp=[[0]*(k+1) for _ in range(n+1)]
for i in range(1,n+1):
    weight[i],value[i]=map(int,sys.stdin.readline().split())

for cur_object in range(1,n+1):
    for limit in range(1,k+1):
        # 물건이 너무 무거워서 limit에 담기지 못할 때
        # 그 물건을 담지 않으면 됨(그 물건을 담지 않고, limit은 같은 이전 단계)
        if weight[cur_object]>limit:
            dp[cur_object][limit]=dp[cur_object-1][limit]
        # 담길 때에는 그 물건을 넣는 경우, 안 넣는 경우를 생각해서
        # 더 큰 걸 선택
        else:
            # 넣는 경우에는 그 물건 weight를 뺀 dp에 그 물건의 value를 더함
            # 안 넣는 경우에는 limit은 유지하면서 그 물건만 넣지 않음
            dp[cur_object][limit]=max(dp[cur_object-1][limit-weight[cur_object]]+value[cur_object],dp[cur_object-1][limit])
print(dp[-1][-1])