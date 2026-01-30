import sys

n,m=map(int,sys.stdin.readline().split())
arr=[]
max_num=0
for _ in range(n):
    arr.append(list(map(int,sys.stdin.readline().split())))

tet=[[(0,1),(0,2),(0,3)],[(1,0),(2,0),(3,0)], # 일자
     [(0,1),(1,0),(1,1)],  # 정사각형
     [(1,0),(2,0),(2,1)],[(0,1),(0,2),(1,0)],[(0,1),(1,1),(2,1)],[(0,1),(0,2),(-1,2)],
     [(1,0),(2,0),(2,-1)],[(0,1),(0,2),(1,2)],[(1,0),(2,0),(0,1)],[(1,0),(1,1),(1,2)], # ㄴ자
     [(1,0),(1,1),(2,1)],[(0,1),(1,0),(1,-1)],[(0,1),(-1,1),(1,0)],[(0,1),(1,1),(1,2)], # ㄹ자
     [(0,1),(0,2),(1,1)],[(1,0),(2,0),(1,-1)],[(0,1),(0,2),(-1,1)],[(1,0),(2,0),(1,1)]
     ]

def calc(i,j,dir):
    ans=0
    ans+=arr[i][j]
    for pos in dir:

        nx=i+pos[0]
        ny=j+pos[1]
        if 0<=nx<n and 0<=ny<m:
            ans+=arr[nx][ny]
        else:
            return 0
    return ans

max_num=0
for i in range(n):
    for j in range(m):
        for dir in tet:
            total=calc(i,j,dir)
            max_num=max(total,max_num)

print(max_num)