import sys
import re

n=int(sys.stdin.readline())

rule=sys.stdin.readline().strip()
rule=rule.replace('*','.*')
rule='^'+rule+'$'


p=re.compile(rule)

for _ in range(n):
    line=sys.stdin.readline().strip()
    if p.match(line):
        print("DA")
    else:
        print("NE")