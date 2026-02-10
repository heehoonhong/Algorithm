import heapq

def solution(jobs):
    answer=[]
    prev_end=0
    min_hq=[]
    
    jobs.sort()
    cnt=0
    i=0
    
    while cnt<len(jobs):
        while i<len(jobs) and jobs[i][0]<=prev_end:
            dur=jobs[i][1]
            req_start=jobs[i][0]
            heapq.heappush(min_hq,(dur,req_start))
            i+=1
        if min_hq:
            dur,req_start=heapq.heappop(min_hq)
            prev_end+=dur
            answer.append(prev_end-req_start)
            cnt+=1
        else:
            prev_end=jobs[i][0]
    return sum(answer)//len(answer)
        
    