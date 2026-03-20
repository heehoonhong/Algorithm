from collections import deque

def solution(order):
    sub_conv=[]
    truck=[]
    main_conv=deque()
    for i in range(len(order)):
        main_conv.append(i+1)
    
    for o in order:
        if main_conv and main_conv[0]!=o:
            if sub_conv:
                if sub_conv[-1]!=o:
                    while main_conv and main_conv[0]!=o:
                        sub_conv.append(main_conv.popleft())
            else:
            
                while main_conv and main_conv[0]!=o:
                    sub_conv.append(main_conv.popleft())
            
        
        if sub_conv and sub_conv[-1]==o:
            truck.append(sub_conv.pop())
        elif main_conv and main_conv[0]==o:
            truck.append(main_conv.popleft())
        
        else:
            break
        
    return len(truck)
        
        
        