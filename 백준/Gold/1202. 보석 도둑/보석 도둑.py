import sys
import heapq
from collections import deque

jewel=[]
bag=[]

n,k=map(int,sys.stdin.readline().split())
for _ in range(n):
    w,p=map(int,sys.stdin.readline().split())
    jewel.append((w,p))
for _ in range(k):
    s=int(sys.stdin.readline())
    bag.append(s)

cnt=0
bag.sort()
jewel.sort(key=lambda x:x[0])

index=0 # 보석 index 관리
max_hq=[]
for i in range(len(bag)):
    while index<n and jewel[index][0]<=bag[i]:
        #print('index= ',index)
        heapq.heappush(max_hq,(-jewel[index][1],jewel[index][0]))
        index+=1
    #print(max_hq)
    # 애초에 들어갈 수 있는 것들이 담겼으니 여기에서 [0]을 pop하고 cnt하면 될 듯
    if max_hq:
        result = heapq.heappop(max_hq)
        cnt = cnt + (-result[0])
        #print(max_hq)

print(cnt)