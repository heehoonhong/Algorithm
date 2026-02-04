import sys

input=sys.stdin.readline
n,r,c=map(int,input().split())
quarter=0
def z(n,r,c,q):
    global quarter
    if n==0:
        return q

    half=2**(n-1)
    if r<half:
        if c<half:
            quarter=1
        else:
            quarter=2
            c-=half
    else:
        if c<half:
            quarter=3
            r-=half
        else:
            quarter=4
            r-=half
            c-=half
    q+=(half**2)*(quarter-1)
    # r,c도 줄였으니까 n도 줄여야지.....
    return z(n-1,r,c,q)
print(z(n,r,c,0))