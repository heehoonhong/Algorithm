from collections import defaultdict

def solution(keymap, targets):
    answer = []
    d=defaultdict(int)
    for key in keymap:
        for i in range(len(key)):
            if d[key[i]]!=0:
                d[key[i]]=min(d[key[i]],i+1)
            else:
                d[key[i]]=i+1
    #print(d)
    for target in targets:
        a=0
        for i in range(len(target)):
            if target[i] not in d.keys():
                a=-1
                break
            else:
                a+=d[target[i]]
        answer.append(a)
    return answer
                
        
        