import sys
input=sys.stdin.readline
n=int(input())
d={}
for _ in range(n):
   s=int(input())
   d[s]=d.get(s,0)+1

datas=sorted(d.items(),key=lambda x:(-x[1],x[0]))
print(datas[0][0])