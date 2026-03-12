from fractions import gcd

def solution(arr):
    num=arr[0]
    for n in arr:
        num=num*n/gcd(n,num)
    return num
        