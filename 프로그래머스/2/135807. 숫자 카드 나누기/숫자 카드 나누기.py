from fractions import gcd

def solution(arrayA, arrayB):
    # 한 배열에서는 모든 숫자를 나눌 수 있지만
    # 다른 배열에서는 모든 숫자를 나눌 수 없는 숫자
    
    def func(arr1,arr2):
        # arr1의 배열에서 최대공약수를 찾고
        # arr2 배열에서 그게 안 나누어떨어지는지 확인
        num1=arr1[0]
        flag=0
        for i in range(1,len(arr1)):
            num1=gcd(num1,arr1[i])
        if num1==1:return 0
        else:
            for i in range(len(arr2)):
                if arr2[i]%num1==0:
                    flag=1
                    break
            # flag==1이면 나누어떨어지므로 안됨
            # 0이어야 함
            if flag==0: return num1
            else: return 0
    
    s1=func(arrayA,arrayB)
    s2=func(arrayB,arrayA)
    if s1!=0 and s2!=0:
        return max(s1,s2)
    else:
        return max(s1,s2)
    