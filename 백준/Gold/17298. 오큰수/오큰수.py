import sys

n=int(sys.stdin.readline())
nums=list(map(int,sys.stdin.readline().split()))
result=[-1]*n
stack=[]
stack.append((nums[0],0))

for i in range(1,n):
    while stack and nums[i]>stack[-1][0]:
        result[stack[-1][1]]=nums[i]
        stack.pop()

    stack.append((nums[i],i))

result[-1]=-1
print(*result)