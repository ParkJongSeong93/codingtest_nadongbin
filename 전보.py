# n개의 나라
# 최대한 많은 나라에 전보를 전달
# 최대로 보내는 나라의 수와 소요되는 시간 구하기

import heapq

INF = int(1e9)

n, m, c = map(int, input().split())

graph = [[] for _ in range(n+1)]
for _ in range(m):
    x, y, z = map(int, input().split())
    # z의 비용으로 x발 y행
    graph[x].append((z, y))

dist_from_c = [INF] * (n+1)
dist_from_c[c] = 0

# 우선순위 큐(작은 값이 먼저 pop됨), +) 큰 값이 먼저 pop되려면 -를 붙여서 넣음
q = []
heapq.heappush(q, (0, c))
while q:
    dist, current = heapq.heappop(q)
    # 큐에 남아있는 쓸모없는 값들(경로가 긴 것들)을 처리하기 위함(모두 continue)
    if dist > dist_from_c[current]:
        continue

    for destination in graph[current]:
        dist_from_current = destination[0]
        dest = destination[1]
        # 출발지로부터 가는 거리보다 current를 거쳐서 가는 경로가 더 짧을 때
        # 합친 거리로 큐에 넣음
        if (dist + dist_from_current) < dist_from_c[dest]:
            heapq.heappush(q, (dist + dist_from_current, dest))
            dist_from_c[dest] = dist + dist_from_current

maxV = 0
cnt = 0
for d in dist_from_c:
    if d == INF:
        continue
    maxV = max(maxV, d)
    cnt += 1

print(cnt-1, maxV)
