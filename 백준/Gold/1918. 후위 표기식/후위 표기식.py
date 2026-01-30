import sys

line=sys.stdin.readline().strip()
stack=[]
result=""

for ch in line:
    if ch.isalpha():
        result+=ch
    elif ch=='(':
        stack.append(ch)
    elif ch==')':
        while stack and stack[-1]!='(':
            result+=stack.pop()
        # 닫는 괄호 제거
        stack.pop()
    elif ch=='*' or ch=='/':
        while stack and (stack[-1]=='*' or stack[-1]=='/'):
            result+=stack.pop()
        stack.append(ch)
    elif ch=='+' or ch=='-':
        # stack[-1]은 나보다 우선순위가 더 높은 것들이니까 pop해서 result에 더해야 함
        while stack and (stack[-1]=='*' or stack[-1]=='/' or stack[-1]=='+' or stack[-1]=='-'):
            result+=stack.pop()
        stack.append(ch)
    #print(stack)

# 다 끝난 뒤에는 stack.pop하기
while stack:
    result+=stack.pop()
print(result)