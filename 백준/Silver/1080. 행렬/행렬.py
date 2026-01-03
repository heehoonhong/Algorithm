import sys

n,m=map(int,sys.stdin.readline().split())

a=[list(map(int,list(sys.stdin.readline().strip())))for _ in range(n)]
b=[list(map(int,list(sys.stdin.readline().strip())))for _ in range(n)]

cnt=0

def convert(r,c,a):
    for i in range(r,r+3):
        for j in range(c,c+3):
            if a[i][j]==0:
                a[i][j]=1
            else:
                a[i][j]=0

for i in range(n-3+1):
    for j in range(m-3+1):
        if a[i][j]!=b[i][j]:
            convert(i,j,a)
            cnt+=1

if a!=b:
    print(-1)
else:
    print(cnt)