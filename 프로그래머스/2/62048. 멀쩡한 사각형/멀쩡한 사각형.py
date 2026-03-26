from fractions import gcd

def solution(w,h):
    ww=w//gcd(w,h)
    hh=h//gcd(w,h)
    return w*h-gcd(w,h)*(ww+hh-1)