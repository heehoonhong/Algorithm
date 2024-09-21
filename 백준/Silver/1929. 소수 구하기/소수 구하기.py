
m, n=map(int,input().split())

for number in range(m,n+1):
    if number==1:
        continue


    for i in range(2,int(number**0.5)+1):
        if number%i==0:
            break
    else: # for문이 잘 실행되었다면
        print(number)