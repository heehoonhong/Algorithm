import sys

input=sys.stdin.readline
n=int(input())
a=[]
for i in range(n):
    a.append(list(map(int,input().split())))
b=0
w=0
def div(r,c,m):
    cnt=0
    global b,w
    for i in range(m):
        cnt+=sum(a[r+i][c:c+m])
    if cnt==m*m:
        b+=1
        return
    elif cnt ==0:
        w+=1
        return

    m=m//2

    # 1
    div(r,c,m)
    # 2
    div(r,c+m,m)
    # 3
    div(r+m,c,m)
    # 4
    div(r+m,c+m,m)

div(0,0,n)
print(w)
print(b)

