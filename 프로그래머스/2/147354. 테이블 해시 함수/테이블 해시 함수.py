from collections import defaultdict

def solution(data, col, row_begin, row_end):
    #print(data)
    data.sort(key=lambda x:(x[col-1],-x[0]))
    #print(data)
    s=defaultdict(int)
    for i in range(row_begin-1,row_end):
        for j in range(len(data[i])):
            s[i+1]+=(data[i][j])%(i+1)
    result=0
    for k in s.keys():
        result^=s[k]
    return result