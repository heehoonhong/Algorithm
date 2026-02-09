import sys

input=sys.stdin.readline
n=int(input())
a=list(map(int,input().split()))
stack=[]
result=[-1]*n
for i in range(len(a)-1):
    # a[i]가 오큰수의 자격이 있는지
    while stack and stack[-1][0]<a[i]:
        result[stack[-1][1]]=a[i]
        stack.pop()
    stack.append((a[i],i))

#print(*stack)
#print(*result)

while stack:
    if stack[-1][0]<a[-1]:
        result[stack[-1][1]]=a[-1]
    else:
        result[stack[-1][1]]=-1
    stack.pop()

#print("==========")
#print(*stack)
print(*result)