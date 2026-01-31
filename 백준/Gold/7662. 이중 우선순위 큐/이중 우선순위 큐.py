import sys
import heapq

t=int(sys.stdin.readline())
for ii in range(t):
    k=int(sys.stdin.readline())
    min_hq = []
    max_hq = []
    visited = [0] * k
    for i in range(k):
        command, num=sys.stdin.readline().split()
        num=int(num)

        if command=="I":
            heapq.heappush(min_hq,(num,i))
            heapq.heappush(max_hq,(-num,i))
            visited[i]=1
        # 가짜 데이터 visited 0, 진짜는 1
        elif command=="D":
            if num==1:
                if max_hq:
                    if visited[max_hq[0][1]]==1:
                        visited[max_hq[0][1]]=0
                        heapq.heappop(max_hq)
                    else:
                        while max_hq and visited[max_hq[0][1]]==0:
                            heapq.heappop(max_hq)
                        if max_hq:
                            visited[max_hq[0][1]]=0
                            heapq.heappop(max_hq)
            elif num==-1:
                if min_hq:
                    if visited[min_hq[0][1]]==1:
                        visited[min_hq[0][1]]=0
                        heapq.heappop(min_hq)
                    else: # max_hq에서 삭제된 유령데이터일 때
                        while min_hq and visited[min_hq[0][1]]==0:
                            heapq.heappop(min_hq)
                        if min_hq:
                            visited[min_hq[0][1]]=0
                            heapq.heappop(min_hq)

    while max_hq and visited[max_hq[0][1]]==0:
        heapq.heappop(max_hq)
    while min_hq and visited[min_hq[0][1]]==0:
        heapq.heappop(min_hq)

    #print("max_hq: ",max_hq)
    #print("min_hq: ", min_hq)
    if max_hq and min_hq:
        print(-max_hq[0][0], min_hq[0][0])
    else:
        print("EMPTY")
