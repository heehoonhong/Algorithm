import heapq

def solution(operations):
    
    deleted=[0]*len(operations)
    min_hq=[]
    max_hq=[]
    for i in range(len(operations)):
        command,num=operations[i].split()
        num=int(num)
        if command=="I":
            heapq.heappush(min_hq,(num,i))
            heapq.heappush(max_hq,(-num,i))
            deleted[i]=1
        elif command=="D":
            
            
            # 최댓값 삭제
            if num==1:
                while min_hq and deleted[min_hq[0][1]]!=1:
                    heapq.heappop(min_hq)
                while max_hq and deleted[max_hq[0][1]]!=1:
                    heapq.heappop(max_hq)
                
                
                if max_hq:
                    deleted[max_hq[0][1]]=0
                    heapq.heappop(max_hq)
                
                
            # 최솟값 삭제
            else:
                while min_hq and deleted[min_hq[0][1]]!=1:
                    heapq.heappop(min_hq)
                while max_hq and deleted[max_hq[0][1]]!=1:
                    heapq.heappop(max_hq)
                if min_hq:
                    deleted[min_hq[0][1]]=0
                    heapq.heappop(min_hq)
                
    result=[]
    while min_hq and deleted[min_hq[0][1]]!=1:
        heapq.heappop(min_hq)
    while max_hq and deleted[max_hq[0][1]]!=1:
        heapq.heappop(max_hq)
    
    if max_hq and deleted[max_hq[0][1]]==1:
        result.append(-heapq.heappop(max_hq)[0])
    else:
        result.append(0)
    
    if min_hq and deleted[min_hq[0][1]]==1:
        result.append(heapq.heappop(min_hq)[0])
    else:
        result.append(0)
    return result
                
            
    