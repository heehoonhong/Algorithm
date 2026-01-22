import sys

n=int(sys.stdin.readline())
arr=[(0,0)]
dp=[[0]*(n+1) for _ in range(n+1)]
for _ in range(n):
    r,c=map(int,sys.stdin.readline().split())
    arr.append((r,c))

for i in range(1,n):
    for j in range(1,n-i+1):
        start=j
        end=j+i
        result=2**31-1
        for k in range(start+1,end+1):
            result1=dp[start][k-1]+dp[k][end]+arr[start][0]*arr[k][0]*arr[end][1]
            result=min(result,result1)
        dp[start][end]=result
#print(dp)
print(dp[1][n])