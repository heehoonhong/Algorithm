import sys

n=int(sys.stdin.readline())
answer=0

def dfs(num):
    global answer
    if len(num)==n:
        answer=int(num)
        return 0


    for i in range(1,4):
        ss=num
        num+=str(i)
        check_flag=True
        for j in range(1,len(num)//2+1):
            if num[len(num)-2*j:len(num)-j]==num[len(num)-j:len(num)]:
                check_flag=False
        if check_flag:
            if dfs(num)==0:
                return 0

        num=ss

flag=dfs("")

print(answer)
