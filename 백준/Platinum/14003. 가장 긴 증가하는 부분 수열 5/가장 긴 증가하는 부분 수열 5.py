import sys
from bisect import bisect_left

n=int(sys.stdin.readline())
a=list(map(int,sys.stdin.readline().split()))
stack=[a[0]]
record=[0]*n
# a[0]이 stack 상에서 0번째에 위치
record[0]=0
for i in range(1,n):
    if stack[-1]<a[i]:
        stack.append(a[i])
        # a[i]가 현재 stack에서 마지막에 위치
        record[i]=len(stack)-1
    else:
        index=bisect_left(stack,a[i])
        stack[index]=a[i]
        # a[i]가 stack 상에서 index 상에 위치
        record[i]=index

target=len(stack)-1
answer=[]
for i in range(n-1,-1,-1):
    if record[i]==target:
        answer.append(a[i])
        target-=1
answer=answer[::-1]
print(len(answer))
print(*answer)

#print(*stack)
#print(*record)