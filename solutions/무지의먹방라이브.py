# 회전판에 먹어야 할 n개의 음식이 있음
# 1초에 앞에서부터 1씩 먹고 다음 음식으로 넘어감
# k초에 네트워크 에러. k초에 어디서부터 먹어야하는지 출력

import heapq

def solution(food_times, k):
    # 불가능한 경우 바로 -1로 반환
    if sum(food_times) <= k:
        return -1
    
    answer = 0

    q = []
    for i in range(1, len(food_times)+1):
        heapq.heappush(q, (food_times[i-1], i))

    sum_value = 0
    previous = 0
    length = len(food_times)

    # sum_value + (현재의 음식 시간 - 이전 음식 시간) * 현재 음식 개수와 k 비교
    while sum_value + ((q[0][0] - previous) * length) <= k:
        now = heapq.heappop(q)[0]
        sum_value += (now - previous) * length
        length -= 1 # 다 먹은 음식 제외
        previous = now # 이전 음식 재설정
    
    # 남은 음식 중에서 몇 번째 음식인지 확인하여 출력
    result = sorted(q, key = lambda x : x[1]) # 음식의 번호 기준으로 정렬
    # k에서 sum_value를 뺀 값이 남은 turn
    # 남은 turn을 계산한 length로 나누고 [1]을 통해 idx를 뽑음
    answer = result[(k - sum_value) % length][1]

    return answer

print(solution([3,1,2], 5))