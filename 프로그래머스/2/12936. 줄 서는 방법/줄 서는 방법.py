from math import factorial

def solution(n, k):
    k-=1
    answer=[]
    numbers=list(range(1,n+1))
    
    while n>0:
        n-=1
        fac=factorial(n)
        idx=k//fac
        answer.append(numbers.pop(idx))
        k=k%fac
    return answer
        