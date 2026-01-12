import sys
import re

rule=re.compile("(10(0)+(1)+|01)+$")

n=int(sys.stdin.readline())
for _ in range(n):
    line=sys.stdin.readline().strip()
    if rule.match(line):
        print("YES")
    else:
        print("NO")