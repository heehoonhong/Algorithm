import sys

a=list(sys.stdin.readline().strip())
target=list(sys.stdin.readline().strip())
stack=[]

for i in range(len(a)):
    stack.append(a[i])
    if len(stack)>=len(target):
        if stack[len(stack)-len(target):len(stack)]==target:
            for _ in range(len(target)):
                stack.pop()
if stack:
    print(''.join(stack))
else:
    print("FRULA")