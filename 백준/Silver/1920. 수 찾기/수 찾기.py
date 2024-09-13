import sys

n=int(sys.stdin.readline())
input_list=list(map(int,sys.stdin.readline().split()))
input_list.sort()

m=int(sys.stdin.readline())
output_list=list(map(int,sys.stdin.readline().split()))

for element in output_list:
    left =0
    right=n-1
    while left<=right:
        mid=(left+right)//2

        if element>input_list[mid]:
            left=mid+1
        elif element<input_list[mid]:
            right=mid-1
        else:
            left=mid
            right=mid
            break    
    if left==mid and right==mid:
        print(1)
    else:
        print(0)
