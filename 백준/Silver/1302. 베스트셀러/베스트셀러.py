n=int(input())
d={}
for _ in range(n):
    s=input()
    d[s]=d.get(s,0)+1

l=[]
for k,v in d.items():
    l.append((k,v))
l.sort(key=lambda x:(-x[1],x[0]))
print(l[0][0])