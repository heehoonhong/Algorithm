n=int(input())

for i in range(n):
    line=input()
    stack=[]

    for element in line:
        if element=='(':
            stack.append('(')
        else:
            if len(stack)==0:
                print("NO")
                break
            else:
                stack.pop()
    else:
        if len(stack)!=0:
            print("NO")
        else:
            print("YES")