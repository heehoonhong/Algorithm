from collections import deque

#
def solution(cacheSize, cities):
    q=deque(maxlen=cacheSize)
    time=0
    for i in range(len(cities)):
        cities[i]=cities[i].lower()
        if cities[i] in q:
            q.remove(cities[i])
            q.append(cities[i])
            time+=1
        else:
            q.append(cities[i])
            time+=5
    return time