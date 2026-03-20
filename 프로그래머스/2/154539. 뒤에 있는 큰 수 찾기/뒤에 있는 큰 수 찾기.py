def solution(numbers):
    answer=[-1]*(len(numbers))
    stack=[]
    # 여기에서 stack은 현재 num보다 큰 수를 저장하기 위한 배열
    # 근데 stack에 인덱스를 저장해야 하는 게 포인트
    # 인덱스를 저장하면 값, 인덱스 둘 다 접근 가능
    for i in range(len(numbers)):
        
        # while문을 만족할 때가 오큰수(뒤큰수)인 경우임
        # 아놔 애초에 스택에 있는 게 인덱스인데 인덱스랑 값을 비교하고 있었네....
        while stack and numbers[stack[-1]]<numbers[i]:
            #print(i,stack)
            index=stack.pop()
            answer[index]=numbers[i]
            
            
        
        stack.append(i)
        
        
    while stack:
        index=stack.pop()
        answer[index]=-1
    
    
    return answer
        