# 1-N번까지의 도시와 m개의 단방향 도로
# X로부터 출발하여 갈 수 있는 도시 중 최단거리가 K인 모든 도시의 번호를 출력

from collections import deque

INF = 1e9

n, m, k, x = map(int, input().split())

graph = [[] for _ in range(n+1)]
for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)

q = deque()
q.append((x, 0))
visited = [False] * (n+1)
visited[x] = True

answer = []

while q:
    current, current_dist = q.popleft()
    for node in graph[current]:
        if visited[node]:
            continue
        q.append((node, current_dist + 1))
        visited[node] = True
        if current_dist + 1 == k:
            answer.append(node)

answer.sort()
if answer:
    for i in answer:
        print(i)
else:
    print(-1)


# 플로이드 워셜은 시간 및 메모리 초과

# dist = [[INF] * (n+1) for _ in range(n+1)]
# for i in range(1, n+1):
#     dist[i][i] = 0

# for i in range(m):
#     a, b = map(int, input().split())
#     dist[a][b] = 1

# for mid in range(1, n+1):
#     for i in range(1, n+1):
#         for j in range(1, n+1):
#             dist[i][j] = min(dist[i][j], dist[i][mid]+dist[mid][j])

# answer = []
# for i in range(1, n+1):
#     if dist[x][i] == k:
#         answer.append(i)

# answer.sort()
# if answer:
#     for i in answer:
#         print(i)
# else:
#     print(-1)
