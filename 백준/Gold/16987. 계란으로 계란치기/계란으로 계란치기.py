import sys

n=int(sys.stdin.readline())
eggs=[]
max_broken_eggs=0
for _ in range(n):
    durability, weight= map(int,sys.stdin.readline().split())
    eggs.append([durability,weight])

def dfs(current_index,eggs):
    cnt=0
    global max_broken_eggs
    if current_index == n:
        for i in range(n):
            if eggs[i][0] <= 0:
                cnt+=1
        max_broken_eggs=max(max_broken_eggs,cnt)
        return
    for i in range(n):
        if current_index != i:
            if eggs[current_index][0] > 0 and eggs[i][0] > 0:
                eggs[current_index][0] = eggs[current_index][0] - eggs[i][1]
                eggs[i][0] = eggs[i][0] - eggs[current_index][1]
                current_index += 1
                dfs(current_index, eggs)
                current_index -= 1
                eggs[current_index][0] += eggs[i][1]
                eggs[i][0] += eggs[current_index][1]
            else:
                current_index += 1
                dfs(current_index, eggs)
                current_index -= 1

dfs(0,eggs)

print(max_broken_eggs)
