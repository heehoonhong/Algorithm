import sys
import heapq

t=int(sys.stdin.readline())
for _ in range(t):
    k=int(sys.stdin.readline())
    arr=list(map(int,sys.stdin.readline().split()))

    min_hq=[]
    for i in range(k):
        heapq.heappush(min_hq,arr[i])

    cost=0
    for i in range(k-1):
        num1=heapq.heappop(min_hq)
        num2=heapq.heappop(min_hq)
        cost+=num1+num2
        heapq.heappush(min_hq,num1+num2)
    print(cost)