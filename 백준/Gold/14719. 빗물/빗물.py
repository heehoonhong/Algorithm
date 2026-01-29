import sys
from collections import deque

h,w=map(int,sys.stdin.readline().split())
blocks=list(map(int,sys.stdin.readline().split()))

bbb=deque()

max_block=0
max_index=0
for i in range(len(blocks)):
    if max_block<blocks[i]:
        max_block=blocks[i]
        max_index=i
bbb.append([max_index,max_block])


while True:
    updated=False

    max_block = 0
    max_index = 0
    for i in range(bbb[0][0]):
        # 이 구간에서 max 찾기
        if max_block < blocks[i]:
            max_block = blocks[i]
            max_index = i
    if max_block!=0:
        bbb.appendleft([max_index, max_block])
        updated=True
    max_block = 0
    max_index = 0
    for i in range(bbb[-1][0] + 1, len(blocks)):
        # 이 구간에서 max 찾기
        if max_block <= blocks[i]:
            max_block = blocks[i]
            max_index = i
    if max_block!=0:
        bbb.append([max_index, max_block])
        updated=True

    if not updated:
        break

cnt=0
#print(*bbb)
for i in range(len(bbb)-1):
    max_num = min(bbb[i][1], bbb[i + 1][1])
    #print("a ",max_num)
    for j in range(bbb[i][0]+1,bbb[i+1][0]):
        cnt+=max_num-blocks[j]
        #print(max_num-blocks[j])

print(cnt)