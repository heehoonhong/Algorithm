import sys
from collections import defaultdict

input=sys.stdin.readline
line=input().strip()
line=line.upper()
d=defaultdict(int)
for l in line:
    d[l]+=1
#print(d)
d=list(d.items())
#print(d)
d.sort(key=lambda x:(-x[1]))
if len(d)>1 and d[0][1]==d[1][1]:
    print("?")
else:
    print(d[0][0])




