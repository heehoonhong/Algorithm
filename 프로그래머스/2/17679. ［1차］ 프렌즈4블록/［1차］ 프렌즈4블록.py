from collections import deque

def solution(m, n, board):
    board=[list(i) for i in board]
    answer=0
    while True:
        remove=set()
        for i in range(m-1):
            for j in range(n-1):
                if board[i][j]==0: continue
                
                if board[i][j]==board[i][j+1]==board[i+1][j]==board[i+1][j+1]:
                    remove.add((i,j))
                    remove.add((i,j+1))
                    remove.add((i+1,j))
                    remove.add((i+1,j+1))
        if not remove: break
        
        answer+=len(remove)
        for i,j in remove:
            board[i][j]=0
        
        for j in range(n):
            temp=[]
            for i in range(m):
                if board[i][j]!=0:
                    temp.append(board[i][j])
            zero_count=m-len(temp)
            new_arr=[0]*zero_count+temp
            
            for i in range(m):
                board[i][j]=new_arr[i]
    return answer
            
            
            
            