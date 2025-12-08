def solution(n):
    
    arr=[0,1]
    
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        for i in range(2,n+1):
            val=arr[i-1]+arr[i-2]
            arr.append(val)
        return arr[-1]%1234567    
    
    answer = 0
    return answer