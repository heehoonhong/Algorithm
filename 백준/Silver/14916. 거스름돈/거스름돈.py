import sys

n=int(sys.stdin.readline())
cnt=0
if n%5==0:
    cnt+=n//5
else:
    max_five=n//5
    while True:

        rest=n-max_five*5
        if rest%2==0:
            cnt += max_five
            cnt += rest // 2
            break
            
        if max_five == 0:
            cnt = -1
            break
        
        max_five-=1
print(cnt)