import sys
from collections import deque

n,m=map(int,sys.stdin.readline().split())
nums=list(map(int,sys.stdin.readline().split()))

nnn=[ i+1 for i in range(n)]
dq=deque(nnn)

cnt=0

for element in nums:

    while dq.index(element)!=0:

        if dq.index(element)<len(dq)-dq.index(element):
            number = dq.popleft()
            dq.append(number)
            cnt += 1
        elif dq.index(element)>=len(dq)-dq.index(element):
            number = dq.pop()
            dq.appendleft(number)
            cnt += 1

    dq.popleft()

print(cnt)
