import sys
import heapq

n=int(sys.stdin.readline())

max_hq=[]
min_hq=[]

for _ in range(n):
    num=int(sys.stdin.readline())

    if len(max_hq)<=len(min_hq):
        heapq.heappush(max_hq,-num)
    else:
        heapq.heappush(min_hq,num)

    if min_hq and -max_hq[0] > min_hq[0]:
        max_val=-heapq.heappop(max_hq)
        min_val=heapq.heappop(min_hq)

        heapq.heappush(max_hq,-min_val)
        heapq.heappush(min_hq,max_val)

    print(-max_hq[0])