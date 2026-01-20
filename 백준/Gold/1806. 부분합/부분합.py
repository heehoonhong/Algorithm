import sys

n,s=map(int,sys.stdin.readline().split())
a=list(map(int,sys.stdin.readline().split()))
l=0
r=0
llen=1
total=a[0]
c=set()
while r<n:
    #print(l,r)

    if total<s:

        r+=1
        if r<n:
            total+=a[r]
        llen+=1
    else:
        total-=a[l]
        c.add(llen)
        l+=1
        llen-=1

if l==0:
    print(0)
else:
    print(min(c))