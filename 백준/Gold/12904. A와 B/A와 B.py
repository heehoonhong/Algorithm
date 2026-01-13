import sys

s=list(sys.stdin.readline().strip())
t=list(sys.stdin.readline().strip())

while len(t)!=len(s):

    if t[-1]=='A':
        t.pop(-1)
    elif t[-1]=='B':
        t.pop(-1)
        t=t[::-1]

if s==t:
    print(1)
else:
    print(0)