import sys
from collections import deque

def search():
    drdc = [(1,0), (0,1), (-1,0), (0,-1)]
    INF = 10**4

    N = int(sys.stdin.readline())
    energy = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
    dist = [[INF] * (N) for _ in range(N)]
    dist[0][0] = energy[0][0]

    q = deque()
    q.append((0, 0))

    while q:
        current_r, current_c = q.popleft()
        current_dist = dist[current_r][current_c]
        for dr, dc in drdc:
            nr = current_r + dr
            nc = current_c + dc
            if nr < 0 or nr >= N or nc < 0 or nc >= N:
                continue
            nxt_dist = current_dist + energy[nr][nc]
            if nxt_dist < dist[nr][nc]:
                dist[nr][nc] = nxt_dist
                q.append((nr, nc))

    print(dist[N-1][N-1])

def main():
    T = int(sys.stdin.readline())
    for _ in range(T):
        search()

main()