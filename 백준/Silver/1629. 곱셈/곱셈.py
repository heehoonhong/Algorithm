import sys

input=sys.stdin.readline
a,b,c=map(int,input().split())
result=a

def calc(b):
    if b==1:
        return a%c
    temp=calc(b//2)
    if b%2==0:
        return (temp*temp)%c
    else:
        return (temp*temp*calc(1))%c
print(calc(b))