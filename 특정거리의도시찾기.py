from collections import deque

n, m, k, x = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)

dist = [-1] * (n + 1)
dist[x] = 0
q = deque([x])

while q:
    cur = q.popleft()
    for nxt in graph[cur]:
        if dist[nxt] == -1:
            dist[nxt] = dist[cur] + 1
            q.append(nxt)

ans = [i for i in range(1, n + 1) if dist[i] == k]
if not ans:
    print(-1)
else:
    for v in ans:
        print(v)
