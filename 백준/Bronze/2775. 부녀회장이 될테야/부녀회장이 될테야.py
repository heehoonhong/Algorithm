a=0
b=0
n=int(input())

for _ in range(n):
    a=int(input())
    b=int(input())
    
    room=[[0]*(b+1) for _ in range(a+1)]

    for i in range(1,b+1):
        room[0][i]=i

    #a, j가 층,  b, i가 호
    for j in range(1,a+1):
        for i in range(1,b+1):
            room[j][i]=sum(room[j-1][:i+1])


    print(room[j][i])