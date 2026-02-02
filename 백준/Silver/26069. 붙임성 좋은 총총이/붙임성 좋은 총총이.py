import sys

input=sys.stdin.readline
n=int(input())
d=set()
d.add("ChongChong")
for _ in range(n):
   a,b=input().split()
   if a in d:

       d.add(b)
   if b in d:
       d.add(a)
#print(d)
print(len(d))