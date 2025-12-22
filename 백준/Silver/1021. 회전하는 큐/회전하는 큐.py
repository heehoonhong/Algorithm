import sys
from collections import deque

n,m=map(int,sys.stdin.readline().split())
nums=list(map(int,sys.stdin.readline().split()))

nnn=[ i+1 for i in range(n)]
dq=deque(nnn)

cnt=0

for element in nums:

    while dq[0] != element:
        if dq.index(element) <= len(dq)//2:
            dq.rotate(-1)
            cnt+=1
        else:
            dq.rotate(1)
            cnt+=1

    dq.popleft()

print(cnt)
