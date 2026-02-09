import heapq

def solution(scoville, K):
    min_hq=[]
    heapq.heapify(scoville)
    cnt=0
    min_hq=scoville
    flag=True
    while min_hq and min_hq[0]<K:
        sco=heapq.heappop(min_hq)
        if min_hq:
            
            sco2=heapq.heappop(min_hq)
            new_sco=sco+2*sco2
            heapq.heappush(min_hq,new_sco)
            cnt+=1
        else:
            flag=False
            break
        #print(min_hq[0])
    if flag:
        return cnt
    else:
        return -1
    