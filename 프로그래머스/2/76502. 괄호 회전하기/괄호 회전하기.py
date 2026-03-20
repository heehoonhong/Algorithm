def solution(s):
    ls=len(s)
    cnt=0
    
    def func(ss):
        stack=[]
        for ch in ss:
            if stack:
                if stack[-1]=='[':
                    if ch==']':
                        stack.pop()
                    elif ch=='(' or ch=='[' or ch=='{':
                        stack.append(ch)
                elif stack[-1]=='(':
                    if ch==')':
                        stack.pop()
                    elif ch=='(' or ch=='[' or ch=='{':
                        stack.append(ch)
                elif stack[-1]=='{':
                    if ch=='}':
                        stack.pop()
                    elif ch=='(' or ch=='[' or ch=='{':
                        stack.append(ch)
                
            else:
                if ch ==')' or ch=='}' or ch==']':
                    return False
                else:
                    stack.append(ch)
        if stack:
            return False
        else:
            return True
    
    for i in range(ls):
        new_s=s[i:]+s[:i]
        #print(new_s)
        result=func(new_s)
        if result==True:
            cnt+=1
        
    return cnt