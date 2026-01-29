import sys
n=int(sys.stdin.readline())
tops=list(map(int,sys.stdin.readline().split()))
result=[0]*n
stack=[]
stack.append((tops[-1],len(tops)-1))
for i in range(n-2,-1,-1):
    while stack and tops[i]>stack[-1][0]:
        #print(stack)
        result[stack[-1][1]]=i+1
        stack.pop()
    stack.append((tops[i],i))


print(*result)