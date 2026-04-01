def solution(s):
    s=s.replace("{{","").replace("}}","").split("},{")
    #print(s)
    # sss=0 ㄴ
    s.sort(key= lambda x:len(x))
    result=[]
    for i in range(len(s)):
        s[i]=s[i].split(",")
        for element in s[i]:
            if int(element) not in result:
                result.append(int(element))
    return result
            
            
        