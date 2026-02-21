import sys

input=sys.stdin.readline
n,b=map(int,input().split())
arr=[]

for _ in range(n):
    a=list(map(int,input().split()))
    arr.append(a)

def mul(arr1,arr2):
    # arr1은 N*M, arr2는 M*K
    M=len(arr1)
    N=len(arr1[0])
    K=len(arr2[0])
    result=[[0]*K for _ in range(N)]
    for i in range(N):
        for j in range(K):
            for kk in range(M):
                result[i][j]+=(arr1[i][kk]*arr2[kk][j])%1000
            result[i][j]%=1000
    return result

def func(a,b):
    if b==1:
        for i in range(n):
            for j in range(n):
                a[i][j]=a[i][j]%1000
        return a
    half=func(a,b//2)
    if b%2==0:
        return mul(half,half)
    else:
        return mul(func(a,1),mul(half,half))

result=func(arr,b)
for i in range(n):
    print(*result[i])