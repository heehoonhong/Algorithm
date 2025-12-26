import sys
import heapq

n=int(sys.stdin.readline())
problems=dict()
max_hq=[]
min_hq=[]
for _ in range(n):
    problem,difficulty=map(int,sys.stdin.readline().split())
    problems[problem]=difficulty
    heapq.heappush(max_hq, (-difficulty, -problem))
    heapq.heappush(min_hq, (difficulty, problem))


m=int(sys.stdin.readline())
for _ in range(m):
    command_list=sys.stdin.readline().split()

    if command_list[0]=="add":
        problem=int(command_list[1])
        difficulty=int(command_list[2])

        problems[problem]=difficulty
        heapq.heappush(max_hq,(-difficulty,-problem))
        heapq.heappush(min_hq,(difficulty,problem))
    elif command_list[0] == "recommend":

        if command_list[1] == "1":
            # [수정] 1. dict에 없거나 OR 2. dict에 있는데 난이도가 다르면 -> 삭제
            while -max_hq[0][1] not in problems or problems[-max_hq[0][1]] != -max_hq[0][0]:
                heapq.heappop(max_hq)
            print(-max_hq[0][1])

        elif command_list[1] == "-1":
            # [수정] 1. dict에 없거나 OR 2. dict에 있는데 난이도가 다르면 -> 삭제
            while min_hq[0][1] not in problems or problems[min_hq[0][1]] != min_hq[0][0]:
                heapq.heappop(min_hq)
            print(min_hq[0][1])

    elif command_list[0]=="solved":
        problems.pop(int(command_list[1]))