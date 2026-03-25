import sys
from collections import deque

input = sys.stdin.readline

def main():
    drdc = [(1, 0), (0, 1), (-1, 0), (0, -1)]

    N, L, R = map(int, input().split())
    world = [list(map(int, input().split())) for _ in range(N)]

    day = 0

    while True:
        groups = []
        visited = [[False] * N for _ in range(N)]

        for r in range(N):
            for c in range(N):
                if visited[r][c]:
                    continue

                q = deque()
                q.append((r, c))
                visited[r][c] = True

                group = [(r, c)]
                nations_sum = world[r][c]

                while q:
                    cr, cc = q.popleft()
                    cur_value = world[cr][cc]

                    for dr, dc in drdc:
                        nr = cr + dr
                        nc = cc + dc

                        if 0 <= nr < N and 0 <= nc < N and not visited[nr][nc]:
                            if L <= abs(cur_value - world[nr][nc]) <= R:
                                visited[nr][nc] = True
                                q.append((nr, nc))
                                group.append((nr, nc))
                                nations_sum += world[nr][nc]

                if len(group) > 1:
                    groups.append((group, nations_sum))

        if not groups:
            break

        day += 1
        for group, nations_sum in groups:
            new_population = nations_sum // len(group)
            for r, c in group:
                world[r][c] = new_population

    print(day)

main()