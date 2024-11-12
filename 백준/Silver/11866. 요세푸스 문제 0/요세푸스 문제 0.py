n,k=map(int,input().split())
num_list=[]
result_list=[]

for i in range(n):
    num_list.append(i+1)

index=0
while num_list!=[]:
    index=(index+k-1)%len(num_list)
    result_list.append(num_list.pop(index))

print("<"+", ".join(map(str,result_list))+">")


