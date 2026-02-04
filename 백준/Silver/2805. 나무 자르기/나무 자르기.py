import sys

input=sys.stdin.readline
n,m=map(int,input().split())
a=list(map(int,input().split()))
h=max(a)
start=0
end=h

while start<end:
    mid=(start+end+1)//2
    ss=sum([s-mid if s>mid else 0 for s in a])
    #print(ss, mid)
    if ss<m:
        end=mid-1
    else:
        start=mid
print(start)