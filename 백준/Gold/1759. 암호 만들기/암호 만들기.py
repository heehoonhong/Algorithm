import sys

input=sys.stdin.readline
l,c=map(int,input().split())
arr=list(input().split())
arr.sort()
la=len(arr)
def dfs(index,s):
    if len(s)==l:
        cnt=0
        cnt2=0
        for ch in s:
            if ch in ('a','e','i','o','u'):
                cnt+=1
            if ch.isalpha() and ch not in ('a','e','i','o','u'):
                cnt2+=1
        if cnt>=1 and cnt2>=2:
            print(s)
        return

    for i in range(index,la):
        dfs(i+1,s+arr[i])
#print(arr)
dfs(0,"")


