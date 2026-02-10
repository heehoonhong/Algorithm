import sys

input=sys.stdin.readline
x=int(input())
n=int(input())
s=0
for _ in range(n):
    money,cnt=map(int,input().split())
    s+=money*cnt
if x==s:
    print("Yes")
else:
    print("No")