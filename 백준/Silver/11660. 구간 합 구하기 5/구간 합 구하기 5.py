import sys

input=sys.stdin.readline
n,m=map(int,input().split())
# arr 원본, arr2 구간 합 배열
arr=[[0]*(n+1) for _ in range(n+1)]
arr2=[[0]*(n+1) for _ in range(n+1)]
for i in range(1,n+1):
    a=[0]+list(map(int,input().split()))
    for j in range(len(a)):
        arr[i][j]=a[j]
for i in range(1,n+1):
    for j in range(1,n+1):
        arr2[i][j]=arr2[i][j-1]+arr2[i-1][j]-arr2[i-1][j-1]+arr[i][j]

for _ in range(m):
    x1,y1,x2,y2=map(int,input().split())
    print(arr2[x2][y2]-arr2[x2][y1-1]-arr2[x1-1][y2]+arr2[x1-1][y1-1])