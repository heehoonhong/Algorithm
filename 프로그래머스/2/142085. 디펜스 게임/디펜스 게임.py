import heapq

def solution(n, k, enemy):
    min_hq=[]
    cnt=0
    i=0
    while i<len(enemy):
        if len(min_hq)<k:
            heapq.heappush(min_hq,enemy[i])
            i+=1
        else:
            if min_hq[0]<enemy[i]:
                num=heapq.heappop(min_hq)
                if n-num>=0:
                    n-=num
                    heapq.heappush(min_hq,enemy[i])
                    i+=1
                else:
                    break
            else:
                if n-enemy[i]>=0:
                    n-=enemy[i]
                    i+=1
                else:
                    break
    return i
                    
                    
                
            