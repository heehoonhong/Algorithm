n=int(input())

result=[]
for i in range(n):
    a,b=map(int,input().split())
    result.append((a,b))

result.sort(key=lambda x: (x[0],x[1]))

for i in range(n):
    print(result[i][0], result[i][1])
