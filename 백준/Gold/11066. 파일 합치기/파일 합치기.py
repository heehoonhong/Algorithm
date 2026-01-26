import sys

t=int(sys.stdin.readline())
for _ in range(t):
    n=int(sys.stdin.readline())
    a=[0]+list(map(int,sys.stdin.readline().split()))
    prefix_sum=[0]*(n+1)

    for i in range(1,n+1):
        prefix_sum[i]=prefix_sum[i-1]+a[i]

    dp=[[0]*(n+1) for _ in range(n+1)]
    for i in range(1,n+1):
        dp[i][i]=0
    for i in range(1,n):
        dp[i][i+1]=a[i]+a[i+1]

    for i in range(2,n):
        for j in range(1,n-i+1):
            result = float('inf')
            start = j
            end = j + i
            for k in range(start, end):
                result1 = dp[start][k] + dp[k + 1][end]
                result = min(result, result1)
            dp[start][end] = result + prefix_sum[end] - prefix_sum[start - 1]

    print(dp[1][n])
