def solution(k, d):
    cnt,y=0,d
    for x in range(0,d+1,k):
        max_y=int((d**2-x**2)**0.5)
        cnt+=(max_y//k)+1
    return cnt