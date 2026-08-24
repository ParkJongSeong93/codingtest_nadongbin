# n x m 크기의 미로에서 탈출해야 함
# 1,1 위치부터 n,m으로 가야함(우리는 0-based로 할 예정)
# 1이 괴물이 없는 부분, 0이 괴물이 있는 부분
# 최소 이동 칸 갯수 출력

from collections import deque

n, m = map(int, input().split())
maze = []
for i in range(n):
    # list 대신 []로 하면 안됨
    # [map(int, input)] 으로 하면 map 객체 하나를 리스트로 감싸는 것
    maze.append(list(map(int, input())))

moves = [(1,0), (-1,0), (0,1), (0,-1)]
q = deque([(0,0)])

while q:
    current = q.popleft()
    for move in moves:
        nr = current[0] + move[0]
        nc = current[1] + move[1]
        if 0<=nr<n and 0<=nc<m and maze[nr][nc] == 1 and (nr,nc) != (0,0):
            q.append((nr,nc))
            maze[nr][nc] = maze[current[0]][current[1]] + 1

print(maze[n-1][m-1])
