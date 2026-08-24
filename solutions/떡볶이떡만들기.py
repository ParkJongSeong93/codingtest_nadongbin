# n은 떡의 갯수, m은 요청한 떡의 길이
# 배열은 떡의 개별 길이, 최대 높이로 잘라서 합이 m이 나오도록
# 파라메트릭 서치 사용(이진 탐색을 하며 조건을 만족하는지 여부 판단) -> 중간 지점부터 잘라보며 더 자를지 덜 자를지 옮겨가봄

n, m = list(map(int, input().split()))
array = list(map(int, input().split()))

start = 0
end = max(array)

result = 0
while(start <= end):
    total = 0
    mid = (start + end) // 2
    for x in array:
        if x > mid:
            # 자른 것들을 더함
            total += x - mid
    if total < m:
        end = mid - 1
    else:
        result = mid
        start = mid + 1

print(result)