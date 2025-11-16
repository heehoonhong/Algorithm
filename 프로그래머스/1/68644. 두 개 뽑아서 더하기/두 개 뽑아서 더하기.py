def solution(numbers):
    answer=set()
    for i in range(len(numbers)):
        for j in range(i,len(numbers)):
            if i!=j:
                answer.add(numbers[i]+numbers[j])
                
    
    return sorted(list(answer))
                