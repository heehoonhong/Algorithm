import sys

n=int(sys.stdin.readline())

tips=[]

for _ in range(n):
    tips.append(int(sys.stdin.readline()))

tips.sort(reverse=True)

optimal_tip=0
for i in range(len(tips)):
    if tips[i]-i>0:
        optimal_tip+=tips[i]-i
print(optimal_tip)