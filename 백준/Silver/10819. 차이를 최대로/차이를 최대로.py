import sys
from itertools import permutations

input=sys.stdin.readline
n=int(input())
a=list(map(int,input().split()))
ans=0
for l in permutations(a):
    total=0
    for i in range(n-1):
        total+=abs(l[i]-l[i+1])
    ans=max(total,ans)
print(ans)