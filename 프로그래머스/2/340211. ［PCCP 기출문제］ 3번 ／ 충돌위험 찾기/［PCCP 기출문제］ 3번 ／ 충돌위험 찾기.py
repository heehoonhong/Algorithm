from collections import defaultdict

def solution(points, routes):
    path=[]
    for i in range(len(routes)):
        route=routes[i]
        time=0
        
        start_x, start_y = points[route[0]-1][0], points[route[0]-1][1]
        path.append((start_x, start_y, time))
        
        for j in range(len(route)-1):
            
            sx,sy=points[route[j]-1][0],points[route[j]-1][1]
            ex,ey=points[route[j+1]-1][0],points[route[j+1]-1][1]
            while sx!=ex:
                
                if sx<ex:
                    sx+=1
                else:
                    sx-=1
                time+=1
                path.append((sx,sy,time))
                
            
            while sy!=ey:
                if sy<ey:
                    sy+=1
                else:
                    sy-=1
                time+=1
                path.append((sx,sy,time))
                
            
    d=defaultdict(list)
    for x,y,time in path:
        d[time].append((x,y))
    #print(d)
    cnt=0
    for k,v in d.items():
        dd=defaultdict(int)
        for element in v:
            if dd[element]==0:
                dd[element]=1
            else:
                dd[element]+=1
        
        for k,v in dd.items():
            if v>=2:
                cnt+=1
                
    return cnt
        
            