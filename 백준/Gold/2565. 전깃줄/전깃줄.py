import sys

n=int(sys.stdin.readline())
a=[]
# i 번째 수를 사용했을 때의 전깃줄 개수
dp=[0]*n
for _ in range(n):
    s,e=map(int,sys.stdin.readline().split())
    a.append((s,e))
a.sort()

for i in range(n):
    max_num=0
    for j in range(i):
        if a[i][1]>a[j][1]:
            max_num=max(max_num,dp[j])
    dp[i]=max_num+1
print(len(a)-max(dp))