def solution(line):
    
    points=set()
    
    for i in range(len(line)):
        for j in range(i+1,len(line)):
            a,b,e=line[i]
            c,d,f=line[j]
            
            if a*d-b*c!=0 :
                if (b*f-e*d)%(a*d-b*c)==0 and (e*c-a*f)%(a*d-b*c)==0:
                    x=(b*f-e*d)//(a*d-b*c)
                    y=(e*c-a*f)//(a*d-b*c)
                    points.add((x,y))
    #points=list(points)
    
    min_x=float('inf')
    max_x=float('-inf')
    min_y=float('inf')
    max_y=float('-inf')
    for point in points:
        min_x=min(min_x,point[0])
        max_x=max(max_x,point[0])
        min_y=min(min_y,point[1])
        max_y=max(max_y,point[1])
    
    result=[]
    for i in range(max_y,min_y-1,-1):
        temp=""
        for j in range(min_x,max_x+1):
            if (j,i) in points:
                temp+="*"
            else:
                temp+="."
        result.append(temp)
    return result
                
                
    
                           