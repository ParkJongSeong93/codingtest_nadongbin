n, c = map(int, input().split())

array = []
for _ in range(n):
    array.append(int(input()))
array.sort()

# 파라메트릭 서치
start = 1                   # 가능한 최소 거리(min gap)
end = array[-1] - array[0]  # 가능한 최대 거리(max gap)
result = 0

while start <= end:
    mid = (start + end) // 2
    value = array[0]
    count = 1

    # 현재의 mid값을 이용해 공유기 설치
    for i in range(1, n):
        if array[i] >= value + mid:
            value = array[i]
            count += 1
    
    # C개 이상의 공유기를 설치할 수 있는 경우, 거리를 증가
    if count >= c:
        start = mid + 1
        result = mid
    # C개 이상의 공유기를 설치할 수 없는 경우, 거리를 감소
    else:
        end = mid - 1

print(result)