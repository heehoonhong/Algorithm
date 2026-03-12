def solution(arr):
    def gcd(n,m):
        if m==0:
            return n
        else:
            return gcd(m,n%m)
    
    def lcm(n,m):
        return n//gcd(n,m)*m    
    
    l=lcm(arr[0],arr[1])
    for i in range(len(arr)-1):
        l=lcm(l,arr[i+1])
    return l
        