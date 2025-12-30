import sys

n,k=map(int,sys.stdin.readline().split())

children=list(map(int,sys.stdin.readline().split()))

children=list(set(children))

children.sort()

adj_height=[]

for i in range(len(children)-1):
    adj_height.append(children[i+1]-children[i])

adj_height.sort()

for _ in range(k-1):
    if adj_height:
        adj_height.pop(-1)

print(sum(adj_height))