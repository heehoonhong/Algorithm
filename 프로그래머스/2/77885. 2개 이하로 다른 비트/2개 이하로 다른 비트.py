def solution(numbers):
    answer=[]
    for num in numbers:
        if num%2==0:
            answer.append(num+1)
        else:
            bin_num= list('0'+bin(num)[2:])
            
            index=''.join(bin_num).rfind('0')
            
            # 이것 때문에 str을 list로 만들어야 함.
            bin_num[index]='1'
            bin_num[index+1]='0'
            
            s=int(''.join(bin_num),2)
            answer.append(s)
    return answer