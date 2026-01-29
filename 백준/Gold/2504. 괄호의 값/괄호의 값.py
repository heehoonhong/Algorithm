import sys

line=sys.stdin.readline().strip()
stack=[]
temp=1
answer=0
error_flag=False
for i in range(len(line)):
    if line[i]=='[':
        temp*=3
        stack.append(line[i])
    elif line[i]=='(':
        temp*=2
        stack.append(line[i])

    elif line[i]==']':
        if not stack or stack[-1]=='(':
            error_flag=True
            break

        if stack and stack[-1]=='[' and line[i-1]=='[':
            answer+=temp
        stack.pop()
        temp=temp//3
    else:
        if not stack or stack[-1]=='[':
            error_flag=True
            break
        if stack and stack[-1]=='(' and line[i-1]=='(':
            answer+=temp
        stack.pop()
        temp=temp//2
    #print(stack)

if stack or error_flag:
    print(0)
else:
    print(answer)