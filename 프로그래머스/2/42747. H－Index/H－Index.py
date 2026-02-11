def solution(citations):
    citations.sort()
    cl=len(citations)
    h_index=0
    for h in range(cl):
        if citations[h]>=cl-h:
            h_index=cl-h
            break
    return h_index