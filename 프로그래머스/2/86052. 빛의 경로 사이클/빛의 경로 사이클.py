def solution(grid):
    R=len(grid)
    C=len(grid[0])
    dx=[-1,0,1,0]
    dy=[0,1,0,-1]
    answer=[]
    visited=[[[0]*4 for _ in range(C)] for _ in range(R)]
    
    for i in range(R):
        for j in range(C):
            for d in range(4):
                if visited[i][j][d]==0:
                    cnt=0
                    r,c,direction=i,j,d
                    
                    while visited[r][c][direction]==0:
                        visited[r][c][direction]=1
                        cnt+=1
                        
                        r=(r+dx[direction])%R
                        c=(c+dy[direction])%C
                        
                        node=grid[r][c]
                        if node=='L':
                            direction=(direction-1)%4
                        elif node=='R':
                            direction=(direction+1)%4
                    answer.append(cnt)
    answer.sort()
    return answer