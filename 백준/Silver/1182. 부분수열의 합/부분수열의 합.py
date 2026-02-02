import sys

input=sys.stdin.readline
n,s=map(int,input().split())
arr=list(map(int,input().split()))
ans=0
result=[]
la=len(arr)
def dfs(index,total,lst):
    global ans
    if index==la:
        if total == s:
            if lst != []:
                result.append(lst)
        return
    # 선택했을 때 안 했을 때 dfs로
    dfs(index+1,total+arr[index],lst+[arr[index]])
    dfs(index+1,total,lst)

dfs(0,0,[])
#print(result)
print(len(result))