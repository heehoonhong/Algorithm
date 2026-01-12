import sys
import re

line=sys.stdin.readline().strip()
rule=re.compile("(10(0)+(1)+|01)+$")

if rule.match(line):
    print("SUBMARINE")
else:
    print("NOISE")