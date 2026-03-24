def solution(dirs):
    cur_x,cur_y=5,5
    visited=[[0]*11 for _ in range(11)]
    visited[5][5]=1
    flag=False
    v=[]
    a=0
    
    for dir in dirs:
        
        flag=False
        # 위
        if dir=='U':
            nx,ny=cur_x+1,cur_y
            if 0<=nx<=10 and 0<=ny<=10:
                sss=abs(cur_x-nx)+abs(cur_y-ny)
                if  (cur_x,cur_y,nx,ny) not in v and (nx,ny,cur_x,cur_y) not in v:
                    if sss>0:
                        a+=1
                        v.append((cur_x,cur_y,nx,ny))
                cur_x,cur_y=nx,ny
        
        # 왼쪽
        elif dir=='L':
            nx,ny=cur_x,cur_y-1
            if 0<=nx<=10 and 0<=ny<=10:
                sss=abs(cur_x-nx)+abs(cur_y-ny)
                if  (cur_x,cur_y,nx,ny) not in v and (nx,ny,cur_x,cur_y) not in v:
                    if sss>0:
                        a+=1
                        v.append((cur_x,cur_y,nx,ny))
                cur_x,cur_y=nx,ny
            
            
        # 아래    
        elif dir=='D':
            nx,ny=cur_x-1,cur_y
            if 0<=nx<=10 and 0<=ny<=10:
                sss=abs(cur_x-nx)+abs(cur_y-ny)
                if  (cur_x,cur_y,nx,ny) not in v and (nx,ny,cur_x,cur_y) not in v:
                    if sss>0:
                        a+=1
                        v.append((cur_x,cur_y,nx,ny))
                cur_x,cur_y=nx,ny
            
        
        # 오른쪽
        else:
            nx,ny=cur_x,cur_y+1
            if 0<=nx<=10 and 0<=ny<=10:
                sss=abs(cur_x-nx)+abs(cur_y-ny)
                if  (cur_x,cur_y,nx,ny) not in v and (nx,ny,cur_x,cur_y) not in v:
                    if sss>0:
                        a+=1
                        v.append((cur_x,cur_y,nx,ny))
                cur_x,cur_y=nx,ny
        
        #print(cur_x,cur_y)
        #print(a)
        #print(v)
        #print(dir)
        #print("=====")
        
            
    ans=0
    for i in range(11):
        ans+=sum(visited[i])
        #print(*visited[i])
    return a