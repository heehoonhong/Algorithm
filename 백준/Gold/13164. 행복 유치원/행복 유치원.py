import sys

n,k=map(int,sys.stdin.readline().split())
children=list(map(int,sys.stdin.readline().split()))
children=list(set(children))
children.sort()

dis=[]
for i in range(len(children)-1):
    dis.append(children[i+1]-children[i])
dis.sort()

for i in range(k-1):
    if dis:
        dis.pop(-1)

print(sum(dis))