n=int(input())

a=list(map(int,input().split()))
b=list(map(int,input().split()))

a.sort()

total=0
for i in range(n):
    b_max=max(b)
    total+=a[i]*b_max
    b.remove(b_max)

print(total)