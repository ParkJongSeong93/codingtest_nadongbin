# 회전판에 먹어야 할 n개의 음식이 있음
# 1초에 앞에서부터 1씩 먹고 다음 음식으로 넘어감
# k초에 네트워크 에러. k초에 어디서부터 먹어야하는지 출력

import heapq

def solution(food_times, k):
    if sum(food_times) <= k:
        return -1
    
    answer = 0

    q = []
    for i in range(len(food_times)):
        heapq.heappush(q, (food_times[i], i+1))

    prev = 0
    survivers = len(q)
    while q:
        food, idx = q[0]
        diff = food - prev

        # 이번 턴에 끝나는 경우
        if diff * survivers > k:
            remains = sorted(q, key = lambda x: x[1])
            return remains[k % survivers][1]
        
        k -= survivers * diff
        survivers -= 1
        prev = food
        heapq.heappop(q)

    return answer

print(solution([3,1,2], 5))