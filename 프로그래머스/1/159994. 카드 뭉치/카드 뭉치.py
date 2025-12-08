def solution(cards1, cards2, goal):
    answer = ''
    answer_list=[]
    result=''
    
    first_index=0
    second_index=0
    
    for i in range(len(goal)):
        if cards1 and goal[i] ==cards1[0]:
            answer_list.append(goal[i])
            del(cards1[0])
        elif cards2 and goal[i] in cards2[0]:
            answer_list.append(goal[i])
            del(cards2[0])
    print(answer_list)
    if answer_list == goal:
        return 'Yes'
    else:
        return 'No'