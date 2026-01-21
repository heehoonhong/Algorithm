import sys
from bisect import bisect_left

n=int(sys.stdin.readline())
A=list(map(int,sys.stdin.readline().split()))
stack=[A[0]]
for a in A[1:]:
    if stack[-1]<a:
        stack.append(a)
    else:
        i=bisect_left(stack,a)
        stack[i]=a
print(len(stack))