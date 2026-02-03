import sys

input=sys.stdin.readline
arr=[]
slst=[]
for _ in range(9):
    arr.append(list(map(int,input().split())))

for i in range(9):
    for j in range(9):
        if arr[i][j]==0:
            slst.append((i,j))

sl=len(slst)

def dfs(depth,slst):
    if depth==sl:
        for i in range(9):
            for j in range(9):
                print(arr[i][j],end=' ')
            print()
        sys.exit(0)

    ci, cj = slst[depth][0], slst[depth][1]
    nums = []
    # 가로 찾기
    for j in range(9):
        nums.append(arr[ci][j])
    # 세로 찾기
    for j in range(9):
        nums.append(arr[j][cj])

    # 구역 찾기
    # 시작 행,열
    r=(ci//3)*3
    c=(cj//3)*3
    for a in range(r,r+3):
        for b in range(c,c+3):
            nums.append(arr[a][b])


    nums = list(set(nums))

    real_nums = []
    for i in range(1, 10):
        if i not in nums:
            real_nums.append(i)

    for num in real_nums:
        arr[ci][cj]=num
        dfs(depth + 1, slst )
        arr[ci][cj]=0

dfs(0,slst)