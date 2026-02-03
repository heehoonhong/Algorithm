import sys

input=sys.stdin.readline
arr=[[0]*9 for _ in range(9)]
for i in range(9):
    line=input().strip()
    for j in range(9):
        arr[i][j] =int(line[j])
tlst=[]
for i in range(9):
    for j in range(9):
        if arr[i][j]==0:
            tlst.append((i,j))
lt=len(tlst)

def dfs(depth,tlst):
    if depth==lt:
        for i in range(9):
            for j in range(9):
                print(arr[i][j],end='')
            print()
        sys.exit()

    ci,cj=tlst[depth][0],tlst[depth][1]
    nums=[]
    for i in range(9):
        nums.append(arr[i][cj])
    for j in range(9):
        nums.append(arr[ci][j])
    r=(ci//3)*3
    c=(cj//3)*3
    for a in range(r,r+3):
        for b in range(c,c+3):
            nums.append(arr[a][b])
    nums=list(set(nums))
    real_nums=[]
    for i in range(1,10):
        if i not in nums:
            real_nums.append(i)

    for num in real_nums:
        arr[ci][cj]=num
        dfs(depth+1,tlst)
        arr[ci][cj]=0

dfs(0,tlst)
