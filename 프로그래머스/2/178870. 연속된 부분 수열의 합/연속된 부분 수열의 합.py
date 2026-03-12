def solution(sequence, k):
    ans=l=r=0
    result=[]
    ##
    while r<len(sequence):
        if ans==k:
            if result==[]:
                result=[l,r-1]
            elif r-1-l<result[1]-result[0]:
                result=[l,r-1]
            
            ans+=sequence[r]
            r+=1
        elif ans>k:
            ans-=sequence[l]
            l+=1
        else:
            ans+=sequence[r]
            r+=1
    while ans>=k:
        if ans==k:
            if result==[]:
                result=[l,r-1]
            elif r-1-l<result[1]-result[0]:
                result=[l,r-1]
        ans-=sequence[l]
        l+=1
        
        
    return result
            