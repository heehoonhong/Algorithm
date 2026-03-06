def solution(n, w, num):
    graph=[[] for _ in range(w)]
    for i in range(n):
        rest=i%w
        if (i//w)%2==0:
            graph[rest].append(i+1)
        else:
            graph[w-1-rest].append(i+1)
    index=0
    for i in range(w):
        if num in graph[i]:
            index=i
            break
    cnt=1
    while graph[index]:
        if graph[index][-1]==num:
            break
        else:
            #print(*graph[index])
            graph[index].pop(-1)
            cnt+=1
    return cnt
    