def solution(babbling):
    answer=0
    can_pronounce=["aya","ye","woo","ma"]
    
    for word in babbling:
        if "ayaaya" in word or "yeye" in word or "woowoo" in word or "mama" in word:
            continue
        
        for cp in can_pronounce:
            word=word.replace(cp," ")
        
        if word.strip()=="":
            answer+=1
    return answer