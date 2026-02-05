import sys

input=sys.stdin.readline
t=int(input())






for _ in range(t):
    f=int(input())
    parent={}
    nums={}
    friend=set()

    def find(x):

        if parent[x]==x:
            return x
        else:
            parent[x]=find(parent[x])
        return parent[x]
    def union(x,y):
        parent_x=find(x)
        parent_y=find(y)

        if parent_x==parent_y:
            print(nums[parent_x])
            return
        elif parent_x<parent_y:
            parent[parent_y]=parent_x
            nums[parent_x]+=nums[parent_y]
            print(nums[parent_x])
        else:
            parent[parent_x]=parent_y
            nums[parent_y]+=nums[parent_x]
            print(nums[parent_y])

    for _ in range(f):
        a,b=input().split()

        if a not in parent:
            parent[a]=a
            nums[a]=1
        if b not in parent:
            parent[b]=b
            nums[b]=1
        union(a,b)
