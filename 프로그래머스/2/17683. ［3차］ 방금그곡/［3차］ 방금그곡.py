def solution(m, musicinfos):
    
    answer="(None)"
    # 음악 제목, 끝난 시각, 악
    # 시작 시각, 끝난 시각, 음악 제목, 악보 정보 ,로 구분
    # 1분에 1개 음
    
    m=m.replace('C#','H')
    m=m.replace('D#','I')
    m=m.replace('F#','J')
    m=m.replace('G#','K')
    m=m.replace('A#','L')
    #print(m)
    max_time=-1
        
        
    
    def func(t):
        times=list(t.split(":"))
        h,m=int(times[0]),int(times[1])
        return 60*h+m
    
    # ,로 나눠서 시간 차이를 구한다음에 
    # dict로 해서 전체 문자열 만들기
    for mi in musicinfos:
        
        mi=mi.replace('C#','H')
        mi=mi.replace('D#','I')
        mi=mi.replace('F#','J')
        mi=mi.replace('G#','K')
        mi=mi.replace('A#','L')
        
        s=list(mi.split(","))
        t1=func(s[0])
        t2=func(s[1])
        l=len(s[3])
        ll=0
        if (t2-t1)%l==0:
            ll=(t2-t1)//l
        else:
            ll=(t2-t1)//l +1
        result=""
        for i in range(ll):
            result+=s[3]
        result=result[:(t2-t1)]
        if m in result:
            if t2-t1>max_time:
                max_time=t2-t1
                answer=s[2]
        
    
    return answer