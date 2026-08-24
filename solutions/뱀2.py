from collections import deque

N = int(input())
K = int(input())

snake = deque()
snake.append((1, 1))
drdc = [(0,1), (1,0), (0,-1), (-1,0)]
dir = 0

apples = set()
for _ in range(K):
    r, c = map(int, input().split())
    apples.add((r, c))

L = int(input())
commands = deque()
for _ in range(L):
    X, C = input().split()
    commands.append((int(X), C))

time = 1
while True:
    nr = snake[-1][0] + drdc[dir][0]
    nc = snake[-1][1] + drdc[dir][1]

    # 벽을 만나거나 자기 몸이 있는 곳이라면 게임 끝
    if nr < 1 or nr > N or nc < 1 or nc > N:
        break
    if (nr, nc) in snake:
        break

    # 새로운 머리 추가
    snake.append((nr, nc))
    
    # 사과가 있는 경우
    if (nr, nc) in apples:
        apples.remove((nr, nc))
    # 사과가 없는 경우
    else:
        snake.popleft()

    if commands:
        X, C = commands[0]
        # 명령 시간과 현재 시간이 동일한 경우
        if time == X:
            commands.popleft()
            if C == 'L':
                dir = (dir + 3) % 4
            elif C == 'D':
                dir = (dir + 1) % 4

    time += 1

print(time)
