def solution(arr1, arr2):
    # arr1은 3*2
    # arr2는 2*2
    n=len(arr1)
    m=len(arr1[0])
    l=len(arr2[0])
    
    result=[[0]*l for _ in range(n)]
    
    for i in range(n):
        for  j in range(m):
            for k in range(l):
                result[i][k]+=(arr1[i][j]*arr2[j][k])
            
    return result
                