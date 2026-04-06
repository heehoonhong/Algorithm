def solution(files):
    arr=[]
    
    for file in files:
        flag=False
        start,end=0,0
        for i in range(len(file)):
            # 숫자 만나기 전
            if not file[i].isdigit() and not flag:
                continue
            elif file[i].isdigit() and not flag:
                start=i
                flag=True
            elif file[i].isdigit() and flag:
                if i-start==5:
                    end=i
                    break
                else:
                    continue
            elif not file[i].isdigit() and flag: 
                end=i
                break
        if end==0: end=len(file) 
                    
        arr.append((start,end))
    f=[]
    for i in range(len(files)):
        s,e=arr[i]
        head,number,tail=files[i][:s],files[i][s:e],files[i][e:]
        f.append((head,number,tail))
    #print(f)
    
    answer=[]
    f.sort(key=lambda x:(x[0].lower(),int(x[1])))
    for i in range(len(f)):
        result=''.join(f[i])
        answer.append(result)
    return answer