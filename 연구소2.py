import sys
from collections import deque
from itertools import combinations

N, M = map(int, sys.stdin.readline().split())

board = []
empty_holes = []
virus_holes = []
drdc = [(1,0), (0,1), (-1,0), (0,-1)]

virus_count = 0
empty_hole_count = 0
wall_count = 0

for r in range(N):
    board.append(list(map(int, sys.stdin.readline().split())))
    for c in range(M):
        if board[r][c] == 0:
            empty_holes.append((r, c))
            empty_hole_count += 1
        elif board[r][c] == 1:
            wall_count += 1
        elif board[r][c] == 2:
            virus_holes.append((r, c))
            virus_count += 1

# 빈칸 3개를 조합으로 뽑고 그 경우들마다 퍼지게 해서 갯수 세어보기
answer = 0
empty_combis = combinations(empty_holes, 3)

for empty_combi in empty_combis:
    temp_board = [[0] * M for _ in range(N)]
    for r in range(N):
        for c in range(M):
            temp_board[r][c] = board[r][c]

    # 막기
    for (r, c) in empty_combi:
        temp_board[r][c] = 1

    # 바이러스 전염
    q = deque()
    for (r, c) in virus_holes:
        q.append((r, c))
    
    new_virus_count = virus_count
    while q:
        r, c = q.popleft()
        for dir in range(4):
            nr = r + drdc[dir][0]
            nc = c + drdc[dir][1]
            if 0<=nr<N and 0<=nc<M and temp_board[nr][nc] == 0:
                temp_board[nr][nc] = 2
                q.append((nr, nc))
                new_virus_count += 1
    
    answer = max(answer, N*M - (wall_count+3) - new_virus_count)

print(answer)