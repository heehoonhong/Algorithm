import sys

n=int(sys.stdin.readline())
num_list=[]

def dfs(current_digit,num):
    if current_digit==-1:
        num_list.append(num)
        return
    # 현재 숫자를 붙이는 경우
    dfs(current_digit-1,int(str(num)+str(current_digit)))
    # 현재 숫자를 붙이지 않는 경우
    dfs(current_digit-1,num)

dfs(9,0)
num_list.sort()
num_list.pop(0)
if n>len(num_list):
    print(-1)
else:
    print(num_list[n-1])
#print(num_list)