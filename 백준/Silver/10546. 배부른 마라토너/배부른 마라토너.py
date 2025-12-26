import sys
from collections import Counter

n=int(sys.stdin.readline())
data1=[]
data2=[]
for _ in range(n):
    data1.append(sys.stdin.readline().strip())


for _ in range(n-1):
    data2.append(sys.stdin.readline().strip())

answer=Counter(data1)-Counter(data2)
print(list(answer.keys())[0])