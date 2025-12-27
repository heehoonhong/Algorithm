import sys
from collections import Counter

runners=[]
complete=[]
n=int(sys.stdin.readline())
for _ in range(n):
    runner=sys.stdin.readline().strip()
    runners.append(runner)
for _ in range(n-1):
    completions=sys.stdin.readline().strip()
    complete.append(completions)

answer=Counter(runners)-Counter(complete)
print(list(answer.keys())[0])