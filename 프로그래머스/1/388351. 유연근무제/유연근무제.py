def solution(schedules, timelogs, startday):
    # 1, 2, 3, 4, 5, 6, 7은 
    # 월 화 수 목  금  토 일
    n=len(schedules)
    total_cnt=0
    for i in range(n):
        hour=schedules[i]//100
        minute=schedules[i]%100
        minute+=10
        if minute>=60:
            minute-=60
            hour+=1
        
        if hour==24:
            hour=0
        
        day=startday
        fromm=schedules[i]
        to=minute+hour*100
        cnt=0
        for timelog in timelogs[i]:
            if timelog<=to or timelog<=fromm:
                if day!=6 and day!=7:
                    cnt+=1            
            day+=1
            if day>7:day=1
        #print(cnt)
        if cnt==5: total_cnt+=1
    
    return total_cnt
        