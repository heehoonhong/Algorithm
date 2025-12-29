import sys

n=int(sys.stdin.readline())
damages=list(map(int,sys.stdin.readline().split()))

damages.sort()
optimal_m=0

if len(damages)%2!=0:
    optimal_m=damages[-1]
    damages.pop(-1)


for i in range(len(damages)//2):
    m=damages[i]+damages[len(damages)-1-i]

    if m>optimal_m:
        optimal_m=m

print(optimal_m)
