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
    
    # 음식 소요시간이 작은 것부터 꺼내기
    # 빠진 것 제외 음식 수를 카운트, 다음으로 작은 음식소요 시간이랑 곱해서 k랑 비교
    rest_num = len(food_times)

    prev_food = 0
    while q:
        food_time, idx = q[0]
        diff = food_time - prev_food

        # 이번 턴에서 걸렸다면
        if diff * rest_num > k:
            q.sort(key= lambda x : x[1])
            return q[k % rest_num][1]
        else:
            k -= diff * rest_num
            rest_num -= 1
            prev_food = food_time
            heapq.heappop(q)

    return answer

print(solution([3,1,2], 5))