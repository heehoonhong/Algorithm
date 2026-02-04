import sys

# 슬라이딩 윈도우: 배열을 전부 저장하지 않고 매번 갱신하기
input=sys.stdin.readline
n=int(input())
arr=list(map(int,input().split()))
dp1=arr
dp2=arr
for _ in range(n-1):
    # 매번 새로 값을 받아 그걸로 dp 갱신
    arr=list(map(int,input().split()))
    dp1=[arr[0]+max(dp1[0],dp1[1]),arr[1]+max(dp1[0],max(dp1[1],dp1[2])),arr[2]+max(dp1[1],dp1[2])]
    dp2=[arr[0]+min(dp2[0],dp2[1]),arr[1]+min(dp2[0],min(dp2[1],dp2[2])),arr[2]+min(dp2[1],dp2[2])]

print(max(dp1),min(dp2))