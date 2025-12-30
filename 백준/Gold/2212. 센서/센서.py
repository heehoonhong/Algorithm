import sys

n=int(sys.stdin.readline())
k=int(sys.stdin.readline())
sensors=list(map(int,sys.stdin.readline().split()))
adj_distance=[]
sensors=set(sensors)
sensors=list(sensors)
sensors.sort()
for i in range(len(sensors)-1):
    adj_distance.append(sensors[i+1]-sensors[i])

adj_distance.sort()

for _ in range(k-1):
    if adj_distance:
        adj_distance.pop(-1)
    

print(sum(adj_distance))