from collections import defaultdict

def solution(lottos, win_nums):
    rank={
        1:6,2:5,3:4,4:3,5:2,6:0
    }
    zero_cnt=0
    cnt=0
    for lotto in lottos:
        if lotto in win_nums:
            cnt+=1
        elif lotto==0:
            zero_cnt+=1
    max_cnt=cnt+zero_cnt
    min_cnt=cnt
    result=[]
    
    if max_cnt==6:
        result.append(1)
    elif max_cnt==5:
        result.append(2)
    elif max_cnt==4:
        result.append(3)
    elif max_cnt==3:
        result.append(4)
    elif max_cnt==2:
        result.append(5)
    else:
        result.append(6)
    
    if min_cnt==6:
        result.append(1)
    elif min_cnt==5:
        result.append(2)
    elif min_cnt==4:
        result.append(3)
    elif min_cnt==3:
        result.append(4)
    elif min_cnt==2:
        result.append(5)
    else:
        result.append(6)
    
    return result