import sys

n,m=map(int,sys.stdin.readline().split())

a=list(map(int,sys.stdin.readline().split()))
l=0
r=0
cnt=0
while r<n:
    #print(l, r)
    total=sum(a[l:r+1])
    if total<m:
        r+=1
    elif total>m:
        l+=1
    else:
        cnt+=1
        r+=1

print(cnt)