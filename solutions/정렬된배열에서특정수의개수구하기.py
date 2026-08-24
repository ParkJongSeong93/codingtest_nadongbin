N, x = map(int, input().split())
data = list(map(int, input().split()))

start_idx = 0
end_idx = N - 1

first = -1
last = -1

while start_idx <= end_idx:
    # 중간지점 구하기
    mid_idx = (start_idx + end_idx) // 2
    mid_value = data[mid_idx]
    if x == mid_value and mid_idx >= 0 and data[mid_idx-1] != mid_value:
        first = mid_idx
        break
    elif x <= mid_value:
        end_idx = mid_idx - 1
    elif x > mid_value:
        start_idx = mid_idx + 1

start_idx = 0
end_idx = N - 1

while start_idx <= end_idx:
    # 중간지점 구하기
    mid_idx = (start_idx + end_idx) // 2
    mid_value = data[mid_idx]
    if x == mid_value and mid_idx < N and data[mid_idx+1] != mid_value:
        last = mid_idx
        break
    elif x < mid_value:
        end_idx = mid_idx - 1
    elif x >= mid_value:
        start_idx = mid_idx + 1

print(-1 if last == -1 and first == -1 else last - first + 1)