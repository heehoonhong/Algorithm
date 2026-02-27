def solution(mats, park):
    answer=-1
    mats.sort(reverse=True)
    col=len(park)
    row=len(park[0])
    
    for mat in mats:
        
        for r in range(col):
            for c in range(row):
                if r+mat>row or c+mat>col: continue
                
                cnt=0
                can_place=False
                for i in range(mat):
                    for j in range(mat):
                        if park[c+i][r+j]=="-1":
                            cnt+=1
                if cnt==mat*mat: can_place=True
                
                if can_place:
                    return mat
                else:
                    continue
    return -1