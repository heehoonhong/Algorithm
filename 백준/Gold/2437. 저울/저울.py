import sys

n=int(sys.stdin.readline())
nums=list(map(int,sys.stdin.readline().split()))
nums.sort()
weight=[]
weight.append(nums[0])

for i in range(1,n):
    if weight[-1]<nums[i]:
        if weight[-1]+1==nums[i]:
            #weight.append(nums[i])
            weight.append(nums[i]+weight[-1])

    else:
        weight.append(weight[-1]+nums[i])
    #print(weight)


if nums[0]!=1:
    print(1)
else:
    print(weight[-1]+1)