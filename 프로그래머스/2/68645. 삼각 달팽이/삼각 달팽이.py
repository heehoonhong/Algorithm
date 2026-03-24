def solution(n):
    # 피라미드의 개수는 1+2+....+n
    # n(n+1)//2 개
    # 1
    # 2 9
    # 3 10 8
    # 4 5  6 7
    # 방향 (1,0),(0,1),(-1,-1)
    arr=[]
    for i in range(n):
        arr.append([0]*(i+1))
    
    
    dx=[1,0,-1]
    dy=[0,1,-1]
    dr=0
    x,y=-1,0
    num=1
    for i in range(n,0,-1):
        # i개만큼 dr 방향으로 값 채우기
        for j in range(i):
            nx,ny=x+dx[dr],y+dy[dr]
            if 0<=nx<n and 0<=ny<n:
                arr[nx][ny]=num
                num+=1
                x,y=nx,ny
        dr=(dr+1)%3
            
    #for i in range(n):
    #    print(*arr[i])
    
    result=[]
    for i in range(n):
        for j in range(len(arr[i])):
            result.append(arr[i][j])
    #return result
    return sum(arr,[])
        
        

    