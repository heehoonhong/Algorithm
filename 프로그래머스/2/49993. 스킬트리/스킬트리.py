def solution(skill, skill_trees):
    
    def topological_sort(s,skill):
        r=""
        for element in s:
            if element in skill:
                r+=element
        
        r=list(r)
        skill=list(skill)
        flag=False
        while r and skill:
            if r[0]==skill[0]:
                r.pop(0)
                skill.pop(0)
            else:
                break
        
        if r==[]:
            flag=True
        
        return flag
        
        
            
                
    
    a=0
    for s in skill_trees:
        flag=topological_sort(s,skill)
        if flag:
            a+=1
    
    return a