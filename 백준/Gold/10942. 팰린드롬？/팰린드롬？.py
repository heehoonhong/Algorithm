import sys

# 1. 입력 받기
n = int(sys.stdin.readline())
# 문자 사이사이에 0(더미)을 끼워넣어 짝수/홀수 처리를 통일합니다.
# 예: [1, 2, 1] -> [0, 1, 0, 2, 0, 1, 0] (여기서 0은 # 역할)
raw = list(map(int, sys.stdin.readline().split()))
a = [0] * (2 * n + 1)
for i in range(n):
    a[2 * i + 1] = raw[i]

# 2. 매내처 알고리즘 (O(N))
# A[i]: i번째 문자를 중심으로 하는 팰린드의 '반지름' 길이
A = [0] * len(a)
p = 0 # 현재 가장 긴 팰린드의 중심
r = 0 # 그 팰린드의 오른쪽 끝 경계

for i in range(len(a)):
    # 1. 초기값 설정: i가 r 안에 있다면, 대칭점(2*p - i)의 정보를 가져옴
    if r >= i:
        A[i] = min(r - i, A[2 * p - i])
    else:
        A[i] = 0
    
    # 2. 중심 확장: 범위를 벗어나지 않는 선에서 양옆 비교
    while i - A[i] - 1 >= 0 and i + A[i] + 1 < len(a) and \
          a[i - A[i] - 1] == a[i + A[i] + 1]:
        A[i] += 1
    
    # 3. 경계 갱신: 새로운 팰린드가 기존 r을 뚫고 나갔다면 업데이트
    if i + A[i] > r:
        r = i + A[i]
        p = i

# 3. 질문 처리 (O(1))
m = int(sys.stdin.readline())
for _ in range(m):
    s, e = map(int, sys.stdin.readline().split())
    # 변환된 배열(a)에서의 인덱스로 매핑
    # 원본 s(1-based) -> 변환 배열의 중심 인덱스 계산
    # 예: 1~3 (1 2 1) -> 변환 배열 인덱스 3 (값 2)이 중심
    center_idx = s + e - 1 
    target_len = e - s + 1
    
    # 해당 중심에서의 최대 반지름(A)이 우리가 원하는 길이(target_len)를 커버하는지 확인
    if A[center_idx] >= target_len:
        print(1)
    else:
        print(0)