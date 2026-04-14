import heapq

def solution(n, works):
    # 야근 피로도: 야근 시작 시점에서 남은 일의 작업량의 제곱
    # 1시간에 작업량 1만큼 처리
    max_hq=[]
    
    for i in range(len(works)):
        heapq.heappush(max_hq,-works[i])
    
    # n번 반복
    for i in range(n):
        num=-heapq.heappop(max_hq)
        if num>0:
            num-=1
            heapq.heappush(max_hq,-num)
        else:
            heapq.heappush(max_hq,-num)
        #print(max_hq)
    answer=0
    while max_hq:
        num=-heapq.heappop(max_hq)
        answer+=num*num
    return answer
    