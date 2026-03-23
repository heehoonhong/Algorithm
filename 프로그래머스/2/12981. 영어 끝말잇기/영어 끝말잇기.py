from collections import defaultdict

def solution(n, words):
    s=[]
    p=defaultdict(list)
    s.append(words[0])
    for i in range(1,len(words)):
        if words[i] not in s and words[i][0]==words[i-1][-1]:
            s.append(words[i])
        else:
            #print(i)
            return [(i%n)+1,(i//n)+1]
    
    return [0,0]