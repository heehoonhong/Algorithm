import sys
import re

t=int(sys.stdin.readline())

p=re.compile("^[A-F]?A+F+C+[A-F]?$")

for _ in range(t):
    line=sys.stdin.readline().strip()

    if p.match(line):
        print("Infected!")
    else:
        print("Good")