import sys

k, n = map(int, sys.stdin.readline().split())
k_list = [int(sys.stdin.readline()) for _ in range(k)]

# 이진 탐색을 위한 초기 범위 설정
left, right = 1, max(k_list)

# 이진 탐색 수행
while left <= right:
    mid = (left + right) // 2  # 중간 값, 자를 랜선 길이
    cnt = sum(lan // mid for lan in k_list)  # 중간 길이로 만들 수 있는 랜선 개수 계산
    
    if cnt >= n:  # 충분히 많은 랜선을 만들 수 있는 경우
        left = mid + 1  # 더 큰 길이로 시도
    else:  # 랜선 개수가 부족한 경우
        right = mid - 1  # 더 짧은 길이로 시도

# 최종적으로 가능한 최대 길이는 right에 저장됨
print(right)
