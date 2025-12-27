import sys

tree=dict()

lines=sys.stdin.readlines()
cnt=0
for line in lines:
    line=line.strip()
    tree[line]=tree.get(line,0)+1
    cnt+=1

sorted_keys=sorted(tree.keys())

for key in sorted_keys:
    print(key,f"{tree[key]/cnt*100:.4f}")