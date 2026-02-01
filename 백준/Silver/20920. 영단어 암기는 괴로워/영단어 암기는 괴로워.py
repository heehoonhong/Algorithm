import sys

n,m=map(int,sys.stdin.readline().split())
d={}
for _ in range(n):
    s=sys.stdin.readline().strip()
    if len(s)>=m:
        d[s]=d.get(s,0)+1

datas=sorted(d.items(),key=lambda x:(-x[1],-len(x[0]),x[0]))

for dd in datas:
    print(dd[0])