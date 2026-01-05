import sys
import heapq

n=int(sys.stdin.readline())
min_hq=[]

for _ in range(n):
    heapq.heappush(min_hq,int(sys.stdin.readline()))

cost=0
for _ in range(n-1):
    num1=heapq.heappop(min_hq)
    num2=heapq.heappop(min_hq)
    cost+=num1+num2
    heapq.heappush(min_hq,num1+num2)
print(cost)