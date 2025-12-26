import sys

n,k=map(int,sys.stdin.readline().split())

a=list(map(int,sys.stdin.readline().split()))
dp=[0]*n
dp[0]=1

for i in range(1,n):
    for j in range(i):
        distance=(i-j)*(1+abs(a[i]-a[j]))
        if distance<=k and dp[j]==1:
            dp[i]=1
            break

if dp[n-1]==1:
    print("YES")
else:
    print("NO")