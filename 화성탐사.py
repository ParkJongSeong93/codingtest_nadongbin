import heapq

drdc = [(1,0), (0,1), (-1,0), (0,-1)]

T = int(input())

for tc in range(T):
    N = int(input())
    mars = []
    for _ in range(N):
        mars.append(list(map(int, input().split())))

    INF = 10**9
    dist = [[INF] * N for _ in range(N)]

    # 시작점
    dist[0][0] = mars[0][0]
    pq = []
    heapq.heappush(pq, (dist[0][0], 0, 0))  # (비용, r, c)

    while pq:
        current_value, current_r, current_c = heapq.heappop(pq)

        # 이미 더 좋은 값으로 갱신된 적 있으면 스킵
        if current_value != dist[current_r][current_c]:
            continue

        # 목적지면 종료(다익스트라는 여기서 확정)
        if current_r == N - 1 and current_c == N - 1:
            break

        for dr, dc in drdc:
            nr = current_r + dr
            nc = current_c + dc
            if nr < 0 or nr >= N or nc < 0 or nc >= N:
                continue

            new_cost = current_value + mars[nr][nc]
            if new_cost < dist[nr][nc]:
                dist[nr][nc] = new_cost
                heapq.heappush(pq, (new_cost, nr, nc))

    print(dist[N-1][N-1])