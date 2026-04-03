def solution(n, k):
    # 지금 만드는 수가 앞에 와야함! 
    answer=''
    while n:
        s=n%k
        answer=str(s)+answer
        n=n//k
    answer=answer.split("0")
    cnt=0
    for i in answer:
        if len(i)==0: continue
        prime=True
        for j in range(2,int(int(i)**0.5+1)):
            if int(i)%j==0:
                prime=False
                break
        if int(i)!=1 and prime:
            cnt+=1
    return cnt
        