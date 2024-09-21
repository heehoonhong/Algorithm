import sys

n=int(sys.stdin.readline())
result=[]

for i in range(n):
    num=int(sys.stdin.readline())
    result.append(num)

result.sort()

for i in range(n):
    print(result[i])