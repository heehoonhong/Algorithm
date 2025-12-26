import sys
from collections import Counter

lines=sys.stdin.readlines()

species=Counter(line.strip() for line in lines)
cnt=sum(species.values())

sorted_keys=sorted(species.keys())

for key in sorted_keys:
    print(key, f"{species[key]/cnt*100:.4f}")