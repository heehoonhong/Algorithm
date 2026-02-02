import sys

input=sys.stdin.readline
k=6

def dfs(index,tlst):
    if len(tlst)==k:
        print(*tlst)
        return
    for i in range(index,len(arr)):
        dfs(i+1,tlst+[arr[i]])

while True:
    line=input().strip()
    arr=list(map(int,line.split()))
    sss=arr[0]
    arr=arr[1:]
    if sss==0:
        break
    dfs(0,[])
    print()
