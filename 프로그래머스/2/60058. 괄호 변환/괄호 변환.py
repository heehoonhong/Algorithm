def check(s):
    stack=[]
    for i in range(len(s)):
        if s[i]=='(':
            stack.append(s[i])
        else:
            if not stack:
                return False
            stack.pop()
    return True

def divide(p):
    left,right=0,0
    for i in range(len(p)):
        if p[i]=='(':
            left+=1
        else:
            right+=1
        if left==right:
            u=p[:i+1]
            v=p[i+1:]
            break
    return u,v
            

def solution(p):
    # 균형잡힌 괄호 문자열: ( 와 ) 개수가 같은 문자열
    # 올바른 괄호 문자열: (, ) 짝도 모두 맞는 문자열
    
    # u, v로 분리
    # u는 균형잡힌 괄호 문자열
    if p=='':
        return ''
    
    u,v=divide(p)
    
    if check(u):
        return u+solution(v)
    else:
        s='('+solution(v)+')'
        for i in range(1,len(u)-1):
            if u[i]=='(':
                s+=')'
            else:
                s+='('
        return s