def solution(players, m, k):
    time=0
    servers=[]
    # 그 시간대에서 이용자가 n*m<=players[time]<(n+1)*m 인지 확인함
    # players[time]을 m으로 나눈 몫
    # 
    cnt=0
    while time<24:
        
        # 서버 증설 해제 과정
        new_servers=[]
        for i in range(len(servers)):
            if time!=servers[i]:
                new_servers.append(servers[i])
        servers.clear()
        servers=new_servers
        
        
        
        
        n=players[time]//m
        # 서버증설이 안 필요한 경우
        if n<=len(servers):
            # 쓸모없는 변수
            s=0
        # 서버 증설이 필요한 경우
        else:
            # 모자란 개수만큼 서버 증설
            for i in range(n-len(servers)):
                servers.append(time+k)
                cnt+=1
            
        #print(time,servers)
        
        time+=1
    #print(cnt)
    return cnt