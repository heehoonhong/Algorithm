def solution(s):
    stack=[]
    flag=True
    for i in range(len(s)):
        if s[i]=='(':
            stack.append(s[i])
        else:
            if stack:
                stack.pop()
            else:
                flag=False
                break
                
            
    if stack or not flag:
        return False
    else:
        return True