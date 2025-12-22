import heapq
import sys

n=int(sys.stdin.readline())

hq=[]

for _ in range(n):
    num=int(sys.stdin.readline())

    if num !=0:
        heapq.heappush(hq,(abs(num),num))
    else:
        if not hq:
            print(0)
        else:
            print(heapq.heappop(hq)[1])