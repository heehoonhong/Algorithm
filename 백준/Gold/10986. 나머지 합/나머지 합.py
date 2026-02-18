import sys
from collections import defaultdict

input=sys.stdin.readline
n,m=map(int,input().split())
a=[0]+list(map(int,input().split()))
arr=[0]*(n+1)
for i in range(1,n+1):
    arr[i]=arr[i-1]+a[i]

rest=[0]*(n+1)
for i in range(1,n+1):
    rest[i]=arr[i]%m

rrest=rest[1:]
#print(rrest)

cnt=defaultdict(int)
answer=0
for r in rrest:
    if r==0:
        answer+=1

    cnt[r]+=1
#print(cnt)
for k,v in cnt.items():
    answer+=(v*(v-1)//2)
print(answer)