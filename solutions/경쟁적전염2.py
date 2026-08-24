import sys

N, K = map(int, sys.stdin.readline().split())

drdc = [(0,1), (1,0), (-1,0), (0,-1)]
viruses = [[] for _ in range(K+1)]

test_board = []
for r in range(N):
    test_board.append(list(map(int, sys.stdin.readline().split())))
    for c in range(N):
        virus = test_board[r][c]
        if virus != 0:
            viruses[virus].append((r, c))

S, X, Y = map(int, sys.stdin.readline().split())
X -= 1
Y -= 1

for time in range(S):
    for i in range(1, K+1):
        if not viruses[i]:
            continue
        new_viruses = []
        for (r, c) in viruses[i]:
            for dir in range(4):
                nr = r + drdc[dir][0]
                nc = c + drdc[dir][1]
                if 0<=nr<N and 0<=nc<N and test_board[nr][nc] == 0:
                    test_board[nr][nc] = i
                    new_viruses.append((nr, nc))
        viruses[i] = new_viruses

print(test_board[X][Y])