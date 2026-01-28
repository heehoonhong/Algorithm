import sys
from collections import deque

t=int(sys.stdin.readline())
for _ in range(t):
    p=sys.stdin.readline().strip()
    n=int(sys.stdin.readline())
    ss=sys.stdin.readline().strip()
    ss=ss[1:-1]
    if n==0:
        queue=deque()
    else:
        queue=deque(ss.split(','))
    error_flag=False
    reverse_flag=False

    #print(*queue)

    for command in p:
        if command == 'R':
            reverse_flag=not reverse_flag
        elif command == 'D':
            if queue:
                if reverse_flag:
                    queue.pop()
                else:
                    queue.popleft()
            else:
                error_flag = True
    if not error_flag:
        if reverse_flag:
            result='['+','.join(list(queue)[::-1])+']'
            print(result)
        else:
            result='['+','.join(queue)+']'
            print(result)
    else:
        print("error")