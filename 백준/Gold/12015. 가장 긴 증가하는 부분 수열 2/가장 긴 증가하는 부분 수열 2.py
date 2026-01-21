import sys
from bisect import bisect_left

n=int(sys.stdin.readline())
A=list(map(int,sys.stdin.readline().split()))
stack=[A[0]]
for i in range(1,n):
    a=A[i]
    if stack[-1]<a:
        stack.append(a)
    else:
        idx=bisect_left(stack,a)
        stack[idx]=a
print(len(stack))