import sys
from collections import defaultdict

input=sys.stdin.readline
k,l=map(int,input().split())
d=defaultdict(int)

for i in range(l):
    line=input().strip()
    d[line]=i

dl=list(d.items())
dl.sort(key=lambda x: (x[1]))
for i in range(min(k,len(dl))):
    print(dl[i][0])