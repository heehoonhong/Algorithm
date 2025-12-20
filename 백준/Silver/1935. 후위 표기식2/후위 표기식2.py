import sys

n=int(sys.stdin.readline())

# ABC*+DE/-
expression=sys.stdin.readline().strip()

# 1 2 3 4 5
nums=[ int(sys.stdin.readline()) for _ in range(n)]

stack=[]

for element in expression:
    if 'A'<= element <= 'Z':
        index=ord(element)-ord('A')
        stack.append(nums[index])

    else:
        right=stack.pop()
        left=stack.pop()

        if element=='*':
            stack.append(left*right)
        elif element=='/':
            stack.append(left / right)
        elif element=='+':
            stack.append(left + right)
        elif element=='-':
            stack.append(left - right)

print(f"{stack.pop():.2f}")