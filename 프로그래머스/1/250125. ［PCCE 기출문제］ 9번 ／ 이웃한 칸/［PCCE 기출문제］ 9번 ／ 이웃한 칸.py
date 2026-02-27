def solution(board, h, w):
    l=len(board)
    dx=[-1,1,0,0]
    dy=[0,0,-1,1]
    cnt=0
    for i in range(4):
        nx=h+dx[i]
        ny=w+dy[i]
        if 0<=nx<l and 0<=ny<l and board[nx][ny]==board[h][w]:
            cnt+=1
    return cnt