import functools

def compare(x,y):
    if x+y>y+x: return 1
    elif x+y==y+x: return 0
    else: return -1

def solution(numbers):
    numbers=list(map(str,numbers))
    numbers.sort(key=functools.cmp_to_key(compare),reverse=True )
    return str(int(''.join(numbers)))