import sys
from collections import deque

n=int(sys.stdin.readline())
tech=list(map(int,sys.stdin.readline().split()))
tech.reverse()

dq=deque()

for i in range(1,n+1):
    skill=tech[i-1]

    if skill==1:
        dq.appendleft(i)
    elif skill==2:
        dq.insert(1,i)
    elif skill==3:
        dq.append(i)

print(*dq)



