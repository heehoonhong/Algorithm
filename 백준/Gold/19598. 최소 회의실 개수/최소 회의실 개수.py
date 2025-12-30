import sys
import heapq

n=int(sys.stdin.readline())
meeting_list=[]
min_hq=[]
for _ in range(n):
    start,end=map(int,sys.stdin.readline().split())
    meeting_list.append((start,end))
meeting_list.sort(key=lambda x:(x[0],x[1]))

heapq.heappush(min_hq,meeting_list[0][1])
for i in range(1,n):
    #회의실 새로 배정해야 하는 경우
    if min_hq[0]>meeting_list[i][0]:
        heapq.heappush(min_hq,meeting_list[i][1])
    else:
        heapq.heappop(min_hq)
        heapq.heappush(min_hq,meeting_list[i][1])
print(len(min_hq))