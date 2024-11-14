n=int(input())

result=1
for i in range(n):
    result=result*(i+1)

result= list(reversed(str(result)))

cnt=0
for i in range(len(result)):
    if result[i]=='0':
        cnt+=1
    else:
        break

print(cnt)
