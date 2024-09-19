import sys
from collections import deque

n = int(sys.stdin.readline().strip())
result_list = deque()  # 큐처럼 사용하기 위해 deque 사용

for i in range(n):
    command = sys.stdin.readline().strip().split()

    if command[0] == "push":
        result_list.append(command[1])
    elif command[0] == "pop":
        if not result_list:
            print(-1)
        else:
            print(result_list.popleft())  # 첫 번째 요소를 제거하고 출력
    elif command[0] == "size":
        print(len(result_list))
    elif command[0] == "empty":
        if not result_list:
            print(1)
        else:
            print(0)
    elif command[0] == "front":
        if not result_list:
            print(-1)
        else:
            print(result_list[0])
    elif command[0] == "back":
        if not result_list:
            print(-1)
        else:
            print(result_list[-1])
