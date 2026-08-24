# 선수 강의가 있는 강의는 선수 강의를 먼저 들어야만 한다.
# 총 n개의 강의를 듣고자 한다. 강의는 1부터 n번까지이다.
# n개의 강의에 대하여 수강하기에 필요한 최소시간 출력

from collections import deque
import copy

v = int(input())

# 각 강의들의 진입차수
indegree = [0] * (v+1)
# 각 강의에 연결된 강의 정보를 담기 위함
graph = [[] for _ in range(v+1)]
# 강의 시간
time = [0] * (v+1)

for i in range(1, v+1):
    data = list(map(int, input().split()))
    time[i] = data[0]
    for x in data[1:-1]:
        indegree[i] += 1
        graph[x].append(i)

# 위상 정렬
def  topology_sort():
    # 배열 등은 주소값만 복사되므로 깊은 복사가 필요
    result = copy.deepcopy(time)
    q = deque()

    for i in range(1, v+1):
        if indegree[i] == 0:
            q.append(i)
    
    while q:
        now = q.popleft()
        for i in graph[now]:
            indegree[i] -= 1
            # 걸리는 시간 계산
            # 가장 최대로 걸리는 선수 과목들을 계산해야 함
            result[i] = max(result[i], result[now] + time[i])
            if indegree[i] == 0:
                q.append(i)
    
    for i in range(1, v+1):
        print(result[i])

topology_sort()