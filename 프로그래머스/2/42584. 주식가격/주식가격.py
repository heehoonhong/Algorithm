def solution(prices):
    stack=[]
    answer=[0]*(len(prices))
    cnt=0
    for i in range(len(prices)):
        
        while stack and prices[stack[-1][0]]>prices[i]:
            index,price=stack.pop()
            answer[index]=i-index
        
        stack.append([i,prices[i]])
    for i in range(len(stack)-1):
        index,price=stack[i][0],stack[i][1]
        if prices[index]==price:
            answer[index]=stack[-1][0]-index
        
    #print(stack)
    return answer
        