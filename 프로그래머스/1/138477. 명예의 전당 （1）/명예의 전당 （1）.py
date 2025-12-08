def solution(k, score):
    original_score=score
    owner_list=[]
    answer = []
    
    for i in range(len(score)):
        owner_list.append(score[i])
        owner_list.sort()
        if i<k:
            answer.append(owner_list[0])
        else:
            
            del(owner_list[0])
            answer.append(owner_list[0])
            
            
    
    return answer