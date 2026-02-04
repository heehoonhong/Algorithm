import sys

input=sys.stdin.readline
n=int(input())
a=list(map(int,input().split()))

n_a=sorted(set(a))

d={}
for i in range(len(n_a)):
    d[n_a[i]]=i
#print(d)

for ele in a:
    print(d[ele], end=' ')