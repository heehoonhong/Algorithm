import sys

lines=sys.stdin.readlines()
species={}
cnt=0
for line in lines:
    tree=line.strip()
    species[tree]=species.get(tree,0)+1
    cnt+=1


sorted_keys=sorted(species.keys())

for key in sorted_keys:
    print(key, f"{species[key]/cnt*100:.4f}")