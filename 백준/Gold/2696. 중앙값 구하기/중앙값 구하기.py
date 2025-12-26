import sys
import heapq

t=int(sys.stdin.readline())

for _ in range(t):
    m=int(sys.stdin.readline())
    arr=[]
    while len(arr)<m:
        line=list(map(int,sys.stdin.readline().split()))
        arr.extend(line)
    min_hq = []
    max_hq = []
    print(round(len(arr)//2)+1)
    for i in range(len(arr)):

        # 어디 힙에 넣을지
        if len(max_hq)<=len(min_hq):
            heapq.heappush(max_hq,-arr[i])
        else:
            heapq.heappush(min_hq,arr[i])


        if min_hq and -max_hq[0]>min_hq[0]:
            max_val=-heapq.heappop(max_hq)
            min_val=heapq.heappop(min_hq)

            heapq.heappush(max_hq,-min_val)
            heapq.heappush(min_hq,max_val)

        if i%2==0:
            print(-max_hq[0], end=' ')
    print()
