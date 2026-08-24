import sys
from collections import deque

input = sys.stdin.readline

N, M, K, X = map(int, input().split())
graph = [[] for _ in range(N+1)]

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)

q = deque()
q.append((X, 0))
visited = [False] * (N+1)
visited[X] = True

answer = []
while q:
    current_node, current_dist = q.popleft()
    if current_dist == K:
        answer.append(current_node)

    for i in graph[current_node]:
        if visited[i]:
            continue
        q.append((i, current_dist + 1))
        visited[i] = True

answer.sort()
if answer:
    for i in answer:
        print(i)
else:
    print(-1)