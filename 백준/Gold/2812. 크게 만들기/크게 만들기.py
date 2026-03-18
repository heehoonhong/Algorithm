import sys

input=sys.stdin.readline
# n-k 자리수의 숫자 출력
# 근데 이 중에서 가장 큰 수려면 앞자리가 가장 커야 함.
# 그래서 stack에 push하고 현재 숫자가 stack[-1]보다 크면 stack.pop()을 해야 함.
# 다른 스택 문제도 동일한 논리니까 비슷한 문제를 많이 풀어야 할 듯?

n,k=map(int,input().split())
s=input().strip()
stack=[]

for num in s:
    # 현재 스택에 있는 숫자가 사라져야 함.
    # 왜냐면 스택으로 완성되는 숫자가 num push하고완성되는 숫자보다 작기 때문에
    while stack and k>0 and stack[-1]<num:
        stack.pop()
        k-=1
    stack.append(num)

if k>0:
    for i in range(k):
        stack.pop()
print(''.join(stack))