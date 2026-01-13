import sys

n=int(sys.stdin.readline())
d=dict()
for _ in range(n):
    line=list(sys.stdin.readline().strip())
    for i in range(len(line)-1,-1,-1):

        d[line[i]]=d.get(line[i],0)+pow(10,len(line)-i-1)

sorted_values=sorted(d.items(),key=lambda x:x[1],reverse=True)
di=dict(sorted_values)

num=9
for  key,value in di.items():
    di[key]=di[key]*num
    num-=1

#print(len(di))
#print(di)
print(sum(di.values()))