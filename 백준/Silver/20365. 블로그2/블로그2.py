import sys
n=int(sys.stdin.readline())
colors=list(sys.stdin.readline().strip())

# 덩어리 개수
colors_group={"B":0,"R":0}

colors_group[colors[0]]+=1

for i in range(1,len(colors)):
    if colors[i]!=colors[i-1]:
        colors_group[colors[i]]+=1

min_group=min(colors_group["B"],colors_group['R'])

print(min(1+min_group,sum(colors_group.values())))