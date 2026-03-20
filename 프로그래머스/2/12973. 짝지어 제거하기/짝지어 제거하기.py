def solution(s):
    stack=[]
    for ch in s:
        if stack:
            if stack[-1]==ch:
                stack.pop()
            else:
                stack.append(ch)
        else:
            stack.append(ch)
    if not stack:
        return 1
    else:
        return 0