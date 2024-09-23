def solution(t,p):
    a_list=[]
    for i in range(len(t)-len(p)+1):
        a_list.append(int(t[i:i+len(p)]))
    cnt=0
    for i in range(len(a_list)):
        if a_list[i]>int(p):
            cnt+=1
    return len(a_list)-cnt
