def divisor(num):
    temp=1
    if num==1:
        return 0
    else:
        # 이렇게 돌면 처음에 나누어떨어지는 수를 찾았을 때
        # 그 몫이 가장 최대가 됨. 
        # 왜냐하면 i가 작은 것부터 도니까
        for i in range(2,int(num**0.5)+1):
            if num%i==0:
                temp=i
                if (num//i)<=10000000:
                    return num//i
                
        return temp

def solution(begin, end):
    answer=[]
    for i in range(begin,end+1):
        answer.append(divisor(i))
    return answer
    
            