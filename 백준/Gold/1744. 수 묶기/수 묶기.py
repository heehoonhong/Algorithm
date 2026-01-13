import sys

n=int(sys.stdin.readline())
p=[]
m=[]
z=[]
mix=[]

for _ in range(n):
    num=int(sys.stdin.readline())
    if num>0:
        p.append(num)
    else:
        m.append(num)

p.sort(reverse=True)
m.sort()

index=0
while index<len(p):
    if index==len(p)-1:
        mix.append(p[index])
        index+=1
    else:
        if p[index] != 1 and p[index + 1] != 1:
            mix.append(p[index] * p[index + 1])
            index += 2
        else:
            mix.append(p[index])
            mix.append(p[index + 1])
            index += 2
#print(mix)
index=0
while index<len(m):
    if index==len(m)-1:
        mix.append(m[index])
        index+=1
    else:
        mix.append(m[index]*m[index+1])
        index+=2
#print(mix)
print(sum(mix))

