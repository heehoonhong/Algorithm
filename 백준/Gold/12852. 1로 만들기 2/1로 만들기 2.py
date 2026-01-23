import sys

n=int(sys.stdin.readline())

dp=[0]*(n+1)
prev_node=[0]*(n+1)

for i in range(2, n + 1):
    dp[i] = dp[i - 1] + 1
    prev_node[i] = i - 1

    if i % 2 == 0:
        if dp[i] > dp[i // 2] + 1:
            dp[i] = dp[i // 2] + 1
            prev_node[i] = i // 2
    if i % 3 == 0:
        if dp[i] > dp[i // 3] + 1:
            dp[i] = dp[i // 3] + 1
            prev_node[i] = i // 3


print(dp[n])
#print(prev_node)

curr=n
answer=[]
while curr!=1:
    answer.append(curr)
    curr=prev_node[curr]
answer.append(curr)
print(*answer)