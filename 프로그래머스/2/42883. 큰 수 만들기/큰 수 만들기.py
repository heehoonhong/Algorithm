def solution(number, k):
    stack=[]
    
    for num in number:
        
        # 왠만하면 큰 수가 가장 앞에 오기 위해서 stack[-1]이랑 비교하면서
        while stack and k>0 and stack[-1]<num:
            stack.pop()
            k-=1
        
        stack.append(num)
    
    if k>0:
        for i in range(k):
            stack.pop()
    
    return ''.join(stack)