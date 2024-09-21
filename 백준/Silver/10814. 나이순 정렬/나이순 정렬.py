n=int(input())

result=[]
for i in range(n):
    a,b=input().split()
    a=int(a)
    result.append((a,b))

result.sort(key=lambda x:(x[0]))

for i in range(n):
    print(result[i][0], result[i][1])

