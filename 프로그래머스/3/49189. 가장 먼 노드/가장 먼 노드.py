import heapq

def solution(n, edge):
    graph=[[] for _ in range(n+1)]
    for i in range(len(edge)):
        s,e=edge[i]
        graph[s].append(e)
        graph[e].append(s)
    
    def dijkstra(start):
        min_hq=[]
        distances={i:float('inf') for i in range(n+1)}
        heapq.heappush(min_hq,(0,start))
        distances[start]=0
        while min_hq:
            current_distance,current_node=heapq.heappop(min_hq)
            if current_distance>distances[current_node]: continue
            
            for next_node in graph[current_node]:
                distance=current_distance+1
                if distance<distances[next_node]:
                    distances[next_node]=distance
                    heapq.heappush(min_hq,(distance,next_node))
        return distances
    
    result=dijkstra(1)
    max_num=0
    for i in range(1,len(result)):
        if result[i]>max_num:
            max_num=result[i]
    cnt=0
    for i in range(1,len(result)):
        if max_num==result[i]: cnt+=1
    return cnt
        
        
        