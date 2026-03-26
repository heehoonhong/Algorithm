import heapq

def solution(N, road, K):
    # 1번 마을에서 음식 주문 가능한 개수
    # 다익스트라로 구한 다음에 result를 돌면서 5이하인 것만 세어야 할 듯?
    
    graph=[[] for _ in range(N+1)]
    for r in road:
        a,b,c=r
        graph[a].append((b,c))
        graph[b].append((a,c))
    
    
    def dijkstra(graph,start):
        distances={i:float('inf') for i in range(N+1)}
        min_hq=[(0,start)]
        
        # start 거리 초기화
        distances[start]=0
        
        while min_hq:
            current_distance,current_node=heapq.heappop(min_hq)
            
            if current_distance>distances[current_node]: continue
            
            for neighbor,weight in graph[current_node]:
                distance=current_distance+weight
                if distance<distances[neighbor]:
                    distances[neighbor]=distance
                    heapq.heappush(min_hq,(distance,neighbor))
        return distances
    
    result=dijkstra(graph,1)
    cnt=0
    #print(type(result))
    #result=result[1:]
    for i in range(1,len(result)):
        if result[i]<=K:
            cnt+=1
    return cnt
                
        
        