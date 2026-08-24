# 음료수 얼려 먹기
# 0이 있는 틀의 갯수를 세는 것

from collections import deque

n, m = map(int, input().split())
data = [input() for _ in range(n)]

answer = 0

visited = [[False]*m for _ in range(n)]

drdc = [(1,0),(-1,0),(0,1),(0,-1)]

for r in range(n):
    for c in range(m):
        if data[r][c] == '1' or visited[r][c]:
            continue
        answer += 1
        q = deque([(r,c)])
        visited[r][c] = True
        while q:
            current = q.popleft()
            for i in range(4):
                nr = current[0] + drdc[i][0]
                nc = current[1] + drdc[i][1]
                # 범위 체크 후 방문 가능한지 체크
                if 0<=nr<n and 0<=nc<m and visited[nr][nc] == False and data[nr][nc] == '0':
                    visited[nr][nc] = True
                    q.append((nr, nc))

print(answer)