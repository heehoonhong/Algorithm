import sys
import heapq

n=int(sys.stdin.readline())
min_hq=[]
for _ in range(n):
    num=int(sys.stdin.readline())
    if num==0:
        if not min_hq:
            print(0)
        else:
            print(heapq.heappop(min_hq)[1])
    else:
        heapq.heappush(min_hq,(abs(num),num))