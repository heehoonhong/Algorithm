import sys

s=sys.stdin.readline().strip()
t=sys.stdin.readline().strip()
s=list(s)
t=list(t)
#print(s)
#print(t)
answer=0
#print(len(s))
#print(len(t))
def dfs(s,t):
    global answer
    if len(s)==len(t):
        if s==t:
            answer= 1
        
    if t:
        if t[len(t) - 1] == 'A':
            dfs(s, t[:len(t) - 1])
        if t[0] == 'B':
            ss=t[1:]
            dfs(s, ss[::-1])


dfs(s,t)
print(answer)
