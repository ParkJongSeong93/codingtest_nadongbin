# 바이러스는 낮은 번호 먼저 퍼짐
# s초 뒤에 x, y에 있는 바이러스의 종류 출력

from collections import deque

n, k = map(int, input().split())

dr = [1,-1,0,0]
dc = [0,0,1,-1]

grid = []
for _ in range(n):
    grid.append(list(map(int, input().split())))

s, x, y = map(int, input().split())
x -= 1
y -= 1

q = deque()
# 큐에 초기 바이러스들 넣기
for r in range(n):
    for c in range(n):
        if grid[r][c] != 0:
            # 마지막 요소는 시간
            q.append((grid[r][c], r, c, 0))

q = sorted(q)
q = deque(q)

# 시간이 지남에 따른 BFS 전염
while q:
    virus, r, c, time = q.popleft()
    if time == s:
        break
    for dir in range(4):
        nr = r + dr[dir]
        nc = c + dc[dir]
        if nr < 0 or nr >= n or nc < 0 or nc >= n:
            continue
        if grid[nr][nc] == 0:
            grid[nr][nc] = virus
            q.append((grid[nr][nc], nr, nc, time + 1))

print(grid[x][y])