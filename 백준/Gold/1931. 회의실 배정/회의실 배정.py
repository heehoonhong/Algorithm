import sys

n=int(sys.stdin.readline())

time_list=[]

answer_list=[]

for _ in range(n):
    start,end=map(int,sys.stdin.readline().split())
    time_list.append((start,end))

time_list.sort(key=lambda x: (x[1],x[0]))
answer_list.append(time_list[0])

index=0
for i in range(1,n):
    if time_list[i][0]>=answer_list[index][1]:
        answer_list.append(time_list[i])
        index+=1

print(len(answer_list))