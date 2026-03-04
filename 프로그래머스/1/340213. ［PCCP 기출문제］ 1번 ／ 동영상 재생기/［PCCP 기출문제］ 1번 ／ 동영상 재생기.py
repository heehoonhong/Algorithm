def solution(video_len, pos, op_start, op_end, commands):
    # commands 가 prev: -> 10초 전 이동(현재 위치가 10초 미만이면 처음 위치, 0분 0초임)
    # commands 가 next: -> 10초 후 이동(남은 위치가 10초 미만이면 마지막 위치로, 동영상의 길이임)
    # commands 가 
    # video_len : 동영상 길이
    # pos: 직전의 재생 위치
    # op_start, op_end: 오프닝 시작 시각, 오프닝 끝나는 시각
    
    # 처음에 현재 pos를 판단해서 op_start, op_end 사이인지를 판단해서 
    # 맞다면 op_end로 이동 후 그 다음 계산 진행
    
    mm,ss=map(int,video_len.split(":"))
    v_time=mm*60+ss
    mm,ss=map(int,pos.split(":"))
    p_time=mm*60+ss
    mm,ss=map(int,op_start.split(":"))
    s_time=mm*60+ss
    mm,ss=map(int,op_end.split(":"))
    e_time=mm*60+ss
    
    for command in commands:
        # 현재 위치가 s_time e_time 사이인지 판단
        if s_time<=p_time<=e_time:
            p_time=e_time
        
        if command=="prev":
            p_time-=10
            if p_time<0:
                p_time=0
        
        elif command=="next":
            p_time+=10
            if p_time>v_time:
                p_time=v_time
    if s_time<=p_time<=e_time:
        p_time=e_time
    
    mm,ss=p_time//60, p_time%60
    #print(mm)
    #print(ss)
    if mm//10==0:
        mm="0"+str(mm)
    if ss//10==0:
        ss="0"+str(ss)
    return str(mm)+":"+str(ss)
    