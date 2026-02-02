import sys
from itertools import combinations_with_replacement

input=sys.stdin.readline
n,m=map(int,input().split())
a=list(map(int,input().split()))
a=set(a)
a=list(a)
a.sort()

for element in combinations_with_replacement(a,m):
    print(*element)