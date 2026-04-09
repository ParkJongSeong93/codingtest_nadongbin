import sys
from collections import deque

def main():
    N, M, K, X = map(int, sys.stdin.readline().split())
    graph = [[] for _ in range(N+1)]

    q = deque()
    q.append((X, 0))
    visited = [False] * (N+1)
    visited[X] = True

    for i in range(M):
        A, B = map(int, sys.stdin.readline().split())
        graph[A].append(B)

    answer = []
    while q:
        current, dist = q.popleft()
        if dist == K:
            answer.append(current)
            continue

        for city in graph[current]:
            if visited[city]:
                continue
            visited[city] = True
            q.append((city, dist+1))

    answer.sort()
    if answer:
        for i in answer:
            print(i)
    else:
        print(-1)

main()