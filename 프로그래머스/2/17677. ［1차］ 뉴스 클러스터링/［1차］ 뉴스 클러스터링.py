def solution(str1, str2):
    arr1=[]
    arr2=[]
    
    for i in range(len(str1)-1):
        s=str1[i:i+2].lower()
        if s.isalpha():
            arr1.append(s)
    
    for i in range(len(str2)-1):
        s=str2[i:i+2].lower()
        if s.isalpha():
            arr2.append(s)
    
    set1=set(arr1)
    set2=set(arr2)
    
    union=set1|set2
    intersection=set1&set2
    
    # 합집합, 교집합 다 구했으니, 이것들을 돌면서 arr1, arr2에 몇 개 있는지 세어줘야 함.
    
    union_len=0
    inter_len=0
    for s in union:
        union_len+=max(arr1.count(s),arr2.count(s))
    for s in intersection:
        inter_len+=min(arr1.count(s),arr2.count(s))
    
    if not union_len and not inter_len:
        return 65536
    else:
        return int(inter_len/union_len*65536)
        
    
    print(union)
    print(intersection)