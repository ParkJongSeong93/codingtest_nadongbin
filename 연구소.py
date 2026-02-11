# 3개의 벽을 세워서 바이러스의 영향을 최소화해야함
# 1은 벽, 0은 빈칸, 2는 바이러스

from collections import deque

n, m = map(int, input().split())
grid = []

for _ in range(n):
    data = list(map(int, input().split()))
    grid.append(data)

dr = [0,0,1,-1]
dc = [1,-1,0,0]

answer = 0

def virus():
    visited = [[False] * m for _ in range(n)]
    q = deque()
    for r in range(n):
        for c in range(m):
            if visited[r][c] is True:
                continue
            if grid[r][c] == 1:
                continue
            if grid[r][c] == 0:
                continue
            q.append((r,c))
            visited[r][c] = True
            while q:
                current_r, current_c = q.popleft()
                for i in range(4):
                    nr = current_r + dr[i]
                    nc = current_c + dc[i]
                    if nr >= n or nr < 0 or nc >= m or nc < 0:
                        continue
                    if visited[nr][nc] == True:
                        continue
                    if grid[nr][nc] == 1 or grid[nr][nc] == 2:
                        continue
                    
                    visited[nr][nc] = True
                    q.append((nr, nc))
    
    result = 0
    for r in range(n):
        for c in range(m):
            if grid[r][c] == 0 and visited[r][c] == False:
                result += 1

    global answer
    answer = max(answer, result)

wall_count = 0

def dfs(start):
    global wall_count
    if wall_count == 3:
        virus()
        return

    for idx in range(start, n * m):
        r = idx // m
        c = idx % m
        if grid[r][c] == 0:
            grid[r][c] = 1
            wall_count += 1
            dfs(idx + 1)
            grid[r][c] = 0
            wall_count -= 1

dfs(0)
print(answer)
