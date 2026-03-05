import sys

input=sys.stdin.readline
n,m,k=map(int,input().split())
graph=[[[] for _ in range(n)] for _ in range(n)]
dx=[-1,-1,0,1,1,1,0,-1]
dy=[0,1,1,1,0,-1,-1,-1]
flst=[]
for _ in range(m):
    x,y,m,s,d=map(int,input().split())
    flst.append((x-1,y-1,m,s,d))

for _ in range(k):
    # 파이어볼의 이동
    for x,y,m,s,d in flst:
        nx=(x+dx[d]*s)%n
        ny=(y+dy[d]*s)%n
        graph[nx][ny].append((m,s,d))
    flst=[]
    for i in range(n):
        for j in range(n):
            if len(graph[i][j])>1:
                cnt=0
                odd_cnt=0
                sum_m,sum_s,sum_d=0,0,0
                dr=[]
                # 각각의 지량,속력, 방향 계산
                while graph[i][j]:
                    m,s,d=graph[i][j].pop(0)
                    cnt+=1
                    sum_m+=m
                    sum_s+=s
                    if d%2==1:
                        odd_cnt+=1


                m,s=sum_m//5,sum_s//cnt
                if odd_cnt==cnt or odd_cnt==0:
                    dr=[0,2,4,6]
                else:
                    dr=[1,3,5,7]

                for ii in range(4):
                    if m!=0:
                        flst.append((i,j,m,s,dr[ii]))

            elif len(graph[i][j])==1:
                m,s,d=graph[i][j].pop()
                flst.append((i,j,m,s,d))
ans=0
for i in range(len(flst)):
    ans+=flst[i][2]
print(ans)