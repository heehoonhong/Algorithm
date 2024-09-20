n = int(input())

time_list = []
answer_list = []

for i in range(n):
    start, end = map(int, input().split())
    to_tuple = (start, end)
    time_list.append(to_tuple)

# 끝나는 시간 기준으로 정렬, 끝나는 시간이 같으면 시작 시간 기준으로 정렬
time_list.sort(key=lambda x: (x[1], x[0]))

# 첫 번째 회의는 항상 선택 가능
k = 0
answer_list.append(time_list[0])

for i in range(1, n):
    # 현재 회의의 시작 시간이 이전에 선택된 회의의 끝나는 시간보다 크거나 같으면 선택
    if time_list[i][0] >= time_list[k][1]:
        answer_list.append(time_list[i])
        k = i  # 마지막으로 선택한 회의를 갱신

# 최대 사용할 수 있는 회의의 개수 출력
print(len(answer_list))
