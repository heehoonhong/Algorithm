import sys

input=sys.stdin.readline
n=int(input())
cnt=0
d=set()

for _ in range(n):
    s=input().strip()
    if s=="ENTER":
        cnt+=len(d)
        d=set()
    else:
        d.add(s)
cnt+=len(d)
print(cnt)