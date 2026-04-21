from collections import defaultdict

def solution(want, number, discount):
    # 마트: 매일 한 가지 상품 할인함
    # 하루에 하나씩만 구매가능
    # 원하는 제품과 수량이 할인하는 날짜와 10일 연속으로 일치
    # -> 회원가입
    products=defaultdict(int)
    for i in range(len(want)):
        products[want[i]]=number[i]
    
    
    def check(pp,arr,index):
        s=0
        
        for i in range(len(arr)):
            p=arr[i]
            if p not in pp.keys():
                s=0
                break
            else:
                if pp[p]>0: 
                    s+=1
                    pp[p]-=1
                    
        #print(s)
        #print(index)
        #print("======")
        if s==10:
            return True
        else:
            return False
            
    answer=0
    for i in range(0,len(discount)-10+1):
        pp=products.copy()
        v=check(pp,discount[i:i+10],i)
        if v: answer+=1
    return answer