import sys
from itertools import permutations

input=sys.stdin.readline
n=int(input())
a=list(map(int,input().split()))
max_num=0
for e in permutations(a):
    elst=list(e)
    cnt=0
    for i in range(n-1):
        cnt+=abs(elst[i]-elst[i+1])
    max_num=max(max_num,cnt)
print(max_num)