import sys

a,b=map(int,sys.stdin.readline().split())

cnt=0
while b>a:
    if b%2==0:
        b=b//2
    elif b%10==1:
        b=b//10
    else: 
        break
    cnt+=1
if b==a:
    print(cnt+1)
else:
    print(-1)