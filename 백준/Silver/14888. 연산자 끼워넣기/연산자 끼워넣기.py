import sys

input=sys.stdin.readline
n=int(input())
a=list(map(int,input().split()))
add,sub,mul,div=map(int,input().split())
min_ans=float('inf')
max_ans=-float('inf')

# depth,


def dfs(depth,add,sub,mul,div,total):
    global n,min_ans,max_ans

    if depth==n:
        min_ans=min(min_ans,total)
        max_ans=max(max_ans,total)
        return

    if add>0:
        dfs(depth+1,add-1,sub,mul,div,total+a[depth])
    if sub>0:
        dfs(depth + 1, add, sub-1, mul, div, total-a[depth])
    if mul>0:
        dfs(depth + 1, add, sub, mul-1, div, total *a[depth])
    if div>0:
        if total<0:
            dfs(depth+1,add,sub,mul,div-1,-((-total)//a[depth]))
        else:

            dfs(depth + 1, add , sub, mul, div-1, total//a[depth])

dfs(1,add,sub,mul,div,a[0])
print(max_ans)
print(min_ans)