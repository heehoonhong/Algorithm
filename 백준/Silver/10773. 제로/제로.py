num_list=[]
n=int(input())

for i in range(n):
    number=int(input())
    if number==0:
        num_list.pop()
    else:
        num_list.append(number)

print(sum(num_list))