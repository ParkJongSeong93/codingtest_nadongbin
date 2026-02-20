N = int(input())
data = list(map(int, input().split()))

start = 0
end = N-1
answer = -1

while start <= end:
    mid = (start + end) // 2
    mid_value = data[mid]
    if mid == mid_value:
        answer = mid
        break
    elif mid > mid_value:
        start = mid + 1
    elif mid < mid_value:
        end = mid - 1

print(answer)