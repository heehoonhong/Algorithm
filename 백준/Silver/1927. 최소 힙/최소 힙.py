import sys
import heapq

n=int(sys.stdin.readline())
hq=[]
for _ in range(n):
    num=int(sys.stdin.readline())
    if num>0:
        heapq.heappush(hq,num)

    elif num==0:
        if hq:
            print(heapq.heappop(hq))
        else:
            print(0)