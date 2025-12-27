import sys
import heapq

n=int(sys.stdin.readline())
max_hq=[]
for _ in range(n):
    num=int(sys.stdin.readline())
    if num>0:
        heapq.heappush(max_hq,-num)
    elif num==0:
        if not max_hq:
            print(0)
        else:
            print(-heapq.heappop(max_hq))