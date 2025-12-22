import heapq
import sys

n=int(sys.stdin.readline())

hq=[]

for _ in range(n):
    nums=list(map(int,sys.stdin.readline().split()))

    for element in nums:
        if len(hq)<n:
            heapq.heappush(hq,element)

        else:
            if hq[0]<element:
                heapq.heappushpop(hq,element)
print(hq[0])

