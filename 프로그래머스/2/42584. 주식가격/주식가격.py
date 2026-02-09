def solution(prices):
    result=[0]*len(prices)
    stack=[]
    stack.append((prices[0],0))
    cnt=1
    for i in range(1,len(prices)):
        if stack[-1][0]<=prices[i]:
            stack.append((prices[i],i))
        else:
            while stack and prices[i]<stack[-1][0]:
                if prices[i]<stack[-1][0]:
                    result[stack[-1][1]]=i-stack[-1][1]
                    stack.pop()
            stack.append((prices[i],i))
    for i in range(len(stack)):
        result[stack[i][1]]=stack[-1][1]-stack[i][1]
    return result
        