def solution(n, t, m, p):
    # 0부터 9까지는 숫자 그대로
    # 10 이
    nums={
        0:'0',1:'1',2:'2',3:'3',4:'4',5:'5',6:'6',7:'7',8:'8',9:'9',
        10:'A',11:'B',12:'C',13:'D',14:'E',15:'F'
    }
    
    
    # number를 n진법으로 변환
    def func(number,n):
        num=""
        while number>0:
            s=number%n
            num+=nums[s]
            number=number//n
        num=num[::-1]
        return num
    
    result="0"
    for i in range(1,100000):
        result+=func(i,n)
    answer=""
    #print(result)
    for i in range(len(result)):
        if (i)%m==(p-1):
            answer+=result[i]
        if len(answer)==t:
            break
    return answer
    
    
    
    
    