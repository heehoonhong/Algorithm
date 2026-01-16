import sys

a=['0']+list(sys.stdin.readline().strip())
b=['0']+list(sys.stdin.readline().strip())
m=len(a)
n=len(b)
dp=[[0]*n for _ in range(m)]
lcs=[]

for i in range(1,m):
    for j in range(1,n):
        if a[i]==b[j]:
            dp[i][j]=dp[i-1][j-1]+1
        else:
            dp[i][j]=max(dp[i-1][j],dp[i][j-1])

x=m-1
y=n-1
while x>0 and y >0:
    if a[x]==b[y]:
        lcs.append(a[x])
        x-=1
        y-=1
    else:
        if dp[x][y-1]>dp[x-1][y]:
            y-=1
        else:
            x-=1
print(dp[-1][-1])
print(''.join(lcs[::-1]))
