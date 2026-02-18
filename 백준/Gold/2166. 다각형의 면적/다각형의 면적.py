import sys

input=sys.stdin.readline
n=int(input())
arr=[]
for i in range(n):
    x,y=map(int,input().split())
    arr.append((x,y))
arr.append(arr[0])
answer=0
for i in range(n):
    answer+= arr[i][0]*arr[i+1][1]-arr[i][1]*arr[i+1][0]
print(abs(answer)/2)