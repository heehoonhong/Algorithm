import sys
import heapq

n=int(sys.stdin.readline())
class_list=[]
min_hq=[]
for _ in range(n):
    start,end=map(int,sys.stdin.readline().split())
    class_list.append((start,end))
class_list.sort(key=lambda x: (x[0],x[1]))
heapq.heappush(min_hq,class_list[0][1])

for i in range(1,n):
    if min_hq[0]>class_list[i][0]:
        heapq.heappush(min_hq,class_list[i][1])
    else:
        heapq.heappop(min_hq)
        heapq.heappush(min_hq,class_list[i][1])
print(len(min_hq))