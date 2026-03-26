def solution(rows, columns, queries):
    graph=[[0]*(columns+1) for _ in range(rows+1)]
    answer=[]
    dx=[0,1,0,-1]
    dy=[1,0,-1,0]
    # 배열 값 삽입
    num=1
    for i in range(1,len(graph)):
        for j in range(1,len(graph[0])):
            graph[i][j]=num
            num+=1
    
    def rotate(graph,query):
        ss=[]
        sx,sy,ex,ey=query
        # 이동할 위치에 있는 변수의 값 임시 저장 변수
        temp=graph[sx][sy]
        ssx,ssy,eex,eey=sx,sy,ex,ey
        # 방향
        for dr in range(4):
            if dr%2==0:
                l=abs(eey-ssy)
            else:
                l=abs(ssx-eex)
            
            for i in range(l):
                nx,ny=sx+dx[dr],sy+dy[dr]
                ss.append(graph[nx][ny])
                temp2=graph[nx][ny]
                graph[nx][ny]=temp
                temp=temp2
                sx,sy=nx,ny
        
        return min(ss)
        
    
    for i in range(len(queries)):
        answer.append(rotate(graph,queries[i]))
    #print(graph)
    return answer