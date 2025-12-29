import sys

n=int(sys.stdin.readline())
ropes=[]
for _ in range(n):
    ropes.append(int(sys.stdin.readline()))

ropes.sort()
optimal_cost=0
for _ in range(n):
    cost=len(ropes)*ropes[0]
    if cost > optimal_cost:
        optimal_cost=cost
    ropes.pop(0)

print(optimal_cost)