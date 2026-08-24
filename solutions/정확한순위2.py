import sys
from collections import deque

def main():
    answer = 0
    N, M = map(int, sys.stdin.readline().split())

    down_score = [set() for _ in range(N + 1)]
    up_score = [set() for _ in range(N + 1)]

    for _ in range(M):
        A, B = map(int, sys.stdin.readline().split())
        down_score[B].add(A)   # B보다 작은 애들
        up_score[A].add(B)     # A보다 큰 애들

    for i in range(1, N + 1):
        count = 1

        down_q = deque([i])
        down_visited = [False] * (N + 1)
        down_visited[i] = True

        while down_q:
            current = down_q.popleft()
            for num in down_score[current]:
                if not down_visited[num]:
                    down_visited[num] = True
                    down_q.append(num)
                    count += 1

        up_q = deque([i])
        up_visited = [False] * (N + 1)
        up_visited[i] = True

        while up_q:
            current = up_q.popleft()
            for num in up_score[current]:
                if not up_visited[num]:
                    up_visited[num] = True
                    up_q.append(num)
                    count += 1

        if count == N:
            answer += 1

    print(answer)

main()