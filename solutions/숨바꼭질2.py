import sys
from collections import deque

def main(): 
    INF = 10**9

    N, M = map(int, sys.stdin.readline().split())
    graph = [[] for _ in range(N+1)]

    for _ in range(M):
        A, B = map(int, sys.stdin.readline().split())
        graph[A].append(B)
        graph[B].append(A)

    visited = [False] * (N+1)
    visited[1] = True
    dist = [INF] * (N+1)
    dist[1] = 0

    q = deque()
    q.append(1)
    while q:
        current = q.popleft()
        current_dist = dist[current]
        for nxt in graph[current]:
            if visited[nxt]:
                continue
            dist[nxt] = current_dist + 1
            q.append(nxt)
            visited[nxt] = True

    barn_num = 0
    barn_dist = 0
    barn_count = 0
    for i in range(1, N+1):
        if dist[i] > barn_dist:
            barn_dist = dist[i]
            barn_count = 1
            barn_num = i
        elif dist[i] == barn_dist:
            barn_count += 1

    print(barn_num, barn_dist, barn_count)

main()