import sys
from collections import deque

a,b=map(int,sys.stdin.readline().split())

queue=deque()
queue.append((a,1))

while queue:
    num,cnt=queue.popleft()
    if num==b:
        print(cnt)
        break
    elif num>b:
        continue
    else:
        queue.append((num*2,cnt+1))
        queue.append((int(str(num)+"1"),cnt+1))
else:
    print(-1)