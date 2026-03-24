def solution(n, left, right):
    arr=[]
    for i in range(left,right+1):
        x=i//n
        y=i%n
        max_num=max(x,y)
        arr.append(max_num+1)
    
    return arr
            
    
