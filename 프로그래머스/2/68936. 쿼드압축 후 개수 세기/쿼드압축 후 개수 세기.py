def solution(arr):
    result={
        0:0, 1:0
    }
    def func(a,r,c,n):
        nonlocal result
        cnt=0
        for i in range(c,c+n):
            for j in range(r,r+n):
                if a[i][j]==1:
                    cnt+=1
        if cnt==0:
            result[0]+=1
            
        elif cnt==n*n:
            result[1]+=1
            
        else:
            half=n//2
            func(a,r,c,half)
            func(a,r+half,c,half)
            func(a,r,c+half,half)
            func(a,r+half,c+half,half)
    func(arr,0,0,len(arr))
    return list(result.values())
            
        
    