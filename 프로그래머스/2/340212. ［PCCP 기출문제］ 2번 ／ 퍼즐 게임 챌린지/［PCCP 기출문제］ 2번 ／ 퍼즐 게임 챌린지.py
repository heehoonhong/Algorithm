def solution(diffs, times, limit):
    time_spent=0
    # diffs[i]: i번째 문제의 난이도(diff)
    # times[i]: i번째 문제의 소요 시간(time_cur), 
    # times[i-1]: i번째에 대해서 이전 문제의 소요시간(time_prev)
    # 나의 숙련도: level
    # if diff<= level -> 
    # if diff > level -> diff - level 번 틀림
    left=1
    right=max(diffs)
    level=1
    ans=level
    while left<=right:
        mid=(left+right)//2
        level=mid
        #print(level)
        time_spent=0
        for i in range(len(diffs)):
            time_cur=times[i]
            # 안 틀리는 경우
            if diffs[i]<=level: 
                
                time_spent+= time_cur
            # 틀리는 경우니까 이전 문제부터 지금 문제까지 모두 틀리고
            # 지금문제의 시간 합산
            else:
                
                temp_time=0
                wrong_cnt=diffs[i]-level
                temp_time+=wrong_cnt*(time_cur+times[i-1])
                temp_time+=time_cur
                time_spent+=temp_time
        #print(time_spent)
        if time_spent<=limit:
            level=mid
            right=mid-1
            ans=mid
            
        else:
            left=mid+1
        
    return ans