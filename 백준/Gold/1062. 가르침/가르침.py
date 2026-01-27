import sys

n,k=map(int,sys.stdin.readline().split())
words=[]
max_count=0
for _ in range(n):
    word=sys.stdin.readline().strip()
    words.append(word)
words_bitmask=[]
for word in words:
    word_bitmask=0
    for ch in word:
        word_bitmask |= 1<<(ord(ch)-ord('a'))
    words_bitmask.append(word_bitmask)

# a,c,i,n,t 가 포함된 base_bitmask 필요
base_bitmask=0
for ch in ['a','c','i','n','t']:
    base_bitmask |= (1<<(ord(ch)-ord('a')))

def dfs(index,count,learned_bitmask):
    global max_count
    if count==k-5:
        read_count=0
        for word_bitmask in words_bitmask:
            # 이 경우에는 word_bitmask가 learned_mask를 포함한다는 뜻!
            # if (word_bitmask&learned_bitmask)==learned_bitmask:
            # A&B==A: A는 B의 부분집합(B가 더 크다)
            # learned_bitmask가 우리가 배워야 하는 최대의 알파벳이니까
            # learned_bitmask가 word_bitmask보다는 당연히 커야 하고
            # word_bitmask가 learned_bitmask의 부분집합이어야 한다.
            if (word_bitmask&learned_bitmask)==word_bitmask:
                read_count+=1
        max_count=max(max_count,read_count)
        return

    for i in range(index,26):
        if not (learned_bitmask & (1<<i)):
            dfs(i+1,count+1,learned_bitmask | (1<<i))

if k<5:
    print(0)
elif k==26:
    print(n)
else:
    dfs(0,0,base_bitmask)
    print(max_count)