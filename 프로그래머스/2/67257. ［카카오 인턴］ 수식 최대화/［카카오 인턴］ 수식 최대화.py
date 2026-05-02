from itertools import permutations

def operation(s1,s2,op):
    if op=='+':
        return str(int(s1)+int(s2))
    elif op=='-':
        return str(int(s1)-int(s2))
    else:
        return str(int(s1)*int(s2))

def calculate(exp,op):
    arr=[]
    temp=""
    for i in exp:
        if i.isdigit():
            temp+=i
        else:
            arr.append(temp)
            arr.append(i)
            temp=""
    arr.append(temp)
    for o in op:
        
        stack=[]
        while len(arr)!=0:
            temp=arr.pop(0)
            if temp==o:
                stack.append(operation(stack.pop(),arr.pop(0),temp))
            else:
                stack.append(temp)
        arr=stack
        
        
        
    return abs(int(arr[0]))
    
def solution(expression):
    op=['*','+','-']
    op=list(permutations(op,3))
    result=[]
    for o in op:
        result.append(calculate(expression,o))
    return max(result)