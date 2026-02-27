def solution(mats, park):
    answer=-1
    mats.sort(reverse=True)
    col=len(park)
    row=len(park[0])
    
    for mat in mats:
        
        for c in range(col):
            for r in range(row):
                if r+mat>row or c+mat>col: continue
                
                
                can_place=False
                if all(park[i][j]=="-1" for i in range(c,c+mat) for j in range(r,r+mat)): can_place= True
                
                
                if can_place:
                    return mat
                else:
                    continue
    return -1