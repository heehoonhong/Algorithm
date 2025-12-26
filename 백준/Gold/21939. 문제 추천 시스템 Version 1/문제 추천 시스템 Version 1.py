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
    elif command_list[0]=="recommend":

        if command_list[1]=="1":

            print(-max_hq[0][1])

        elif command_list[1]=="-1":
            print(min_hq[0][1])

    elif command_list[0]=="solved":
        problem=int(command_list[1])
        if problem==-max_hq[0][1]:
            heapq.heappop(max_hq)

        if problem==min_hq[0][1]:
            heapq.heappop(min_hq)
        problems.pop(problem)