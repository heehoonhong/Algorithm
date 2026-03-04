def solution(bandage, health, attacks):
    attack={}
    for ele1, ele2 in attacks:
        attack[ele1]=ele2
    
    
    
    last_attack_time=attacks[-1][0]
    cur_health=health
    max_health=health
    success_cnt=0
    for i in range(1,last_attack_time+1):
        if i in attack.keys():
            success_cnt=0
            cur_health-=attack[i]
            
        else:
            success_cnt+=1
            if cur_health>=max_health:
                cur_health=max_health
            elif cur_health<=0:
                return -1
            else:
                cur_health+=bandage[1]
                if success_cnt==bandage[0]:
                    cur_health+=bandage[2]
                    success_cnt=0
    if cur_health<=0:
        return -1
    else:
        return cur_health
                
            
        
        
        