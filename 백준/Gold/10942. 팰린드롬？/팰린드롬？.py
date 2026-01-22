import sys

n=int(sys.stdin.readline())
a=[0]+list(map(int,sys.stdin.readline().split()))

dp=[[0]*(n+1) for _ in range(n+1)]
# len이 1
for i in range(1,n+1):
    dp[i][i]=1
# len이 2
for i in range(1,n):
    if a[i]==a[i+1]:
        dp[i][i+1]=1
# len이 3 이상인 경우
for i in range(1,n+1):
    s,e=i-1,i+1
    while s>=1 and e<=n:
        if dp[s+1][e-1]==1:
            if a[s]==a[e]:
                dp[s][e]=1
            else:
                dp[s][e]=0
        else:
            dp[s][e]=0
        s-=1
        e+=1
    s,e=i-1,i+1+1
    while s>=1 and e<=n:
        if dp[s+1][e-1]==1:
            if a[s]==a[e]:
                dp[s][e]=1
            else:
                dp[s][e]=0
        else:
            dp[s][e]=0
        s-=1
        e+=1

m=int(sys.stdin.readline())
for _ in range(m):
    start,end=map(int,sys.stdin.readline().split())
    print(dp[start][end])