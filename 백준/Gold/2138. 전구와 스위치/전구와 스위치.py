import sys

n=int(sys.stdin.readline())
current=list(map(int,list(sys.stdin.readline().strip())))
current2=current[:]
goal=list(map(int,list(sys.stdin.readline().strip())))

# current는 0번 바꿈
# current2는 0번 안 바꿈

cnt=0
cnt2=0

can_flag=True
for i in range(n):
    if i==0:
        for j in range(0,2):
            current[j]=1-current[j]
        cnt+=1
    elif i==n-1:
        if current[i-1]!=goal[i-1] and current[i]!=goal[i]:
            cnt+=1
        elif current[i-1]==goal[i-1] and current[i]==goal[i]:
            continue
        else:
            can_flag=False
    else:
        if current[i-1]!=goal[i-1]:
            for j in range(i-1,i+2):
                current[j]=1-current[j]
            cnt+=1

can_flag2=True
for i in range(n):
    if i==0:
        continue
    elif i == n - 1:
        if current2[i - 1] != goal[i - 1] and current2[i] != goal[i]:
            cnt2 += 1
        elif current2[i - 1] == goal[i - 1] and current2[i] == goal[i]:
            continue
        else:
            can_flag2 = False
    else:
        if current2[i-1]!=goal[i-1]:
            for j in range(i-1,i+2):
                current2[j]=1-current2[j]
            cnt2+=1

if can_flag==False and can_flag2==False:
    print(-1)
elif can_flag==False and can_flag2==True:
    print(cnt2)
elif can_flag==True and can_flag2==False:
    print(cnt)
else:
    print(min(cnt,cnt2))