import sys

N, C = map(int , sys.stdin.readline().split())
houses = [int(sys.stdin.readline()) for _ in range(N)]
houses.sort()

def find_max_dist(houses, C):
    start = 1                       # 최소 인접 공유기 거리
    end = houses[-1] - houses[0]    # 최대 인접 공유기 거리
    result = 0

    while start <= end:
        mid = (start + end) // 2    # 인접 공유기 거리를 탐색
        value = houses[0]           # 첫 설치 공유기
        count = 1                   # 설치 공유기 카운트

        # 공유기 설치
        for i in range(1, len(houses)):
            if houses[i] >= value + mid:
                count += 1
                value = houses[i]
        
        # 설치 횟수와 공유기 갯수 비교
        if count >= C:
            start = mid + 1
            result = mid
        elif count < C:
            end = mid - 1

    return result

print(find_max_dist(houses, C))
        