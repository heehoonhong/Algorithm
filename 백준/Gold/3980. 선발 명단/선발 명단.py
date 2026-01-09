import sys
from collections import deque

def dfs(powers,depth):
    global max_powers
    if depth==11:
        max_powers=max(max_powers,powers)
        return
    for i in range(11):
        if players[depth][i]>0 and i not in players_location:
            powers+=players[depth][i]
            players_location.append(i)
            dfs(powers,depth+1)
            powers-=players[depth][i]
            players_location.pop()

c=int(sys.stdin.readline())

for _ in range(c):
    players=[]
    players_location=deque()
    max_powers=0
    for _ in range(11):
        player=list(map(int,sys.stdin.readline().split()))
        players.append(player)
    dfs(0, 0)
    print(max_powers)