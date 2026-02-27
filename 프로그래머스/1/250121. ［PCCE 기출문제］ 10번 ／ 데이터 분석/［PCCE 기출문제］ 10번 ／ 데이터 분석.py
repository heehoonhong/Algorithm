def solution(data, ext, val_ext, sort_by):
    answer=[]
    s={ "code":0,
        "date":1,
        "maximum":2,
        "remain":3}
    
    index=s[ext]
    for i in range(len(data)):
        if data[i][index]<val_ext:
            answer.append(data[i])
    sort_index=s[sort_by]
    answer.sort(key=lambda x:x[sort_index])
    return answer