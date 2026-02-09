from collections import deque

def solution(bridge_length, weight, truck_weights):
    cnt=0
    tw=deque(truck_weights)
    bridge=deque([0]*bridge_length)
    after=deque()
    cur_weight=0
    while tw or cur_weight!=0:
        
        # 1. bridge에서 트럭 꺼내고, 0 이상이면 append        
        truck=bridge.popleft()
        cur_weight-=truck
        if truck>0:
            after.append(truck)
        if tw and cur_weight+tw[0]<=weight:
            truck=tw.popleft()
            bridge.append(truck)
            cur_weight+=truck
        else:
            bridge.append(0)
        cnt+=1
        #print(bridge)
    return cnt
        
        