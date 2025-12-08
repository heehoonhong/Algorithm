def solution(k, score):
    original_score=score
    owner_list=[]
    answer = []
    
    for i in range(len(score)):
        if i<k:
            owner_list.append(score[i])
            owner_list.sort()
            answer.append(owner_list[0])
        else:
            owner_list.append(score[i])
            owner_list.sort()
            del(owner_list[0])
            answer.append(owner_list[0])
            
            
    
    return answer