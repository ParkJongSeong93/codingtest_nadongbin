from collections import deque
import sys

N, M, K, X = map(int, sys.stdin.readline().split())

graph = [[] for _ in range(N+1)]
visited = [False] * (N+1)
q = deque()
q.append((0, X))
visited[X] = True
distance = [-1] * (N+1)
distance[X] = 0

for _ in range(M):
    start_city, end_city = map(int, sys.stdin.readline().split())
    graph[start_city].append(end_city)

while q:
    dist, city = q.popleft()

    if dist > K:
        break

    for destination in graph[city]:
        if visited[destination]:
            continue
        visited[destination] = True
        q.append((dist+1, destination))
        distance[destination] = dist+1

found = False
for i in range(1, N+1):
    if distance[i] == K:
        print(i)
        found = True

if not found:
    print(-1)
    
