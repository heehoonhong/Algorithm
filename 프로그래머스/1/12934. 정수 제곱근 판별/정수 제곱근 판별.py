def solution(n):
    sqr=n**(1/2)
    if sqr%1==0: return (sqr+1)**2

    else: 
        return -1