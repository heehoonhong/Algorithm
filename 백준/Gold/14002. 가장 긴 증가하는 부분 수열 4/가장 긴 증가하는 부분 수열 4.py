import sys

n=int(sys.stdin.readline())
seq=[0]+list(map(int,sys.stdin.readline().split()))
dp=[0]*(n+1)
prev_node=[0]*(n+1)

for i in range(1,n+1):
    max_num=0
    for j in range(i):
        if seq[i]>seq[j]:
            if max_num<dp[j]:
                max_num=dp[j]
                prev_node[i]=j
    dp[i]=max_num+1

max_num=0
max_index=0
for i in range(1,n+1):
    if max_num<dp[i]:
        max_num=dp[i]
        max_index=i
answer=[]
curr=max_index
while curr!=0:
    answer.append(seq[curr])
    curr=prev_node[curr]
answer=answer[::-1]
print(len(answer))
print(*answer)
