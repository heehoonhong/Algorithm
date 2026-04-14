import heapq

def solution(book_time):
    
    def func(hour):
        hour,minute=hour.split(":")
        h,m=int(hour),int(minute)
        return h*60+m
    lst=[]
    for bt in book_time:
        s,e=bt
        start,end=func(s),func(e)
        lst.append((start,end))
    
    lst.sort(key= lambda x:(x[0]))
    min_hq=[]
    for i in range(len(lst)):
        s,e=lst[i]
        if not min_hq:
            heapq.heappush(min_hq,(e,s))
        else:
            # min_hq에는 e,s 로 저장됨
            # 만약 현재 시간이 min_hq의 끝나는시간보다 
            if min_hq[0][0]+10>s:
                heapq.heappush(min_hq,(e,s))
            else:
                heapq.heappop(min_hq)
                heapq.heappush(min_hq,(e,s))
    return len(min_hq)