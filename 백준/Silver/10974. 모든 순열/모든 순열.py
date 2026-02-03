import sys
from itertools import permutations

input=sys.stdin.readline
n=int(input())
a=list(range(1,n+1))

for e in permutations(a):
    d=list(e)
    print(*d)