import sys

answer=0
n=int(sys.stdin.readline())
nums=[ sys.stdin.readline().strip() for _ in range(n)]

for num in nums:
    stack=[]
    for element in num:
        if not stack:
            stack.append(element)
        elif stack[-1]==element:
            stack.pop()
        else:
            stack.append(element)
    if not stack: answer+=1

print(answer)