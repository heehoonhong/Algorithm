import sys

input=sys.stdin.readline
n,m=map(int,input().split())

a=list(range(n))
parent=list(range(n))

# x의 parent를 찾는 함수
def find(x):
    if x==parent[x]:
        return x
    else:
        parent[x]=find(parent[x])
    return parent[x]

# x와 y의 parent를 같게 만들어 합침.
def union(x,y):
    parent_x=find(x)
    parent_y=find(y)

    if parent_x==parent_y:
        return
    # parent_x 쪽으로 합쳐야 함.(작은 쪽으로)
    elif parent_x<parent_y:
        parent[parent_y]=parent_x
    else:
        parent[parent_x]=parent_y

flag=True
for index in range(m):
    a,b=map(int,input().split())
    parent_a,parent_b=find(a),find(b)
    # union 하기 전에 parent가 같다는 건 사이클이 발생했다는 거임
    if parent_a==parent_b:
        # cycle
        flag=False
        print(index+1)
        break
    else:
        union(a,b)

if flag:
    print(0)