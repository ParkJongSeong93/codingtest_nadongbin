# 뱀이 벽 또는 자기 자신과 부딪히면 게임 끝
# n x n 보드 위에서 진행, 좌상단에서 시작, 뱀의 초기길이는 1
# 처음에는 오른쪽으로 향함
# 1. 먼저 뱀은 몸길이를 늘려 머리를 다음 칸에 위치
# 2. 이동한 칸에 사과가 있다면, 사과가 없어지고 꼬리는 움직이지 않음
# 3. 이동한 칸에 사과가 없다면, 몸길이를 줄여서 꼬리가 위치한 칸을 비움
# 게임이 몇 초에 끝나는지 출력

from collections import deque

n = int(input())

timer_count = 0

board = [[0] * (n+1) for _ in range(n+1)]
# 북,동,남,서
dir = [(-1,0), (0,1), (1, 0), (0,-1)]
snake_dir = 1

snake = deque()
snake.appendleft((1,1))

def check_body_or_wall(nr, nc):
    if nr > n or nr < 1 or nc > n or nc < 1:
        return False
    elif (nr, nc) in snake:
        return False
    return True

def snake_move(move_dir):
    nr = snake[0][0] + dir[move_dir][0]
    nc = snake[0][1] + dir[move_dir][1]
    if check_body_or_wall(nr, nc):
        snake.appendleft((nr, nc))
        if board[nr][nc]:
            board[nr][nc] = 0
            return True
        else:
            snake.pop()
            return True
    else:
        return False


# 사과의 개수
k = int(input())
for i in range(k):
    r, c = map(int, input().split())
    board[r][c] = 1

l = int(input())
action_list = []
for i in range(l):
    x, c = input().split()
    action_list.append((int(x), c))

while True:
    timer_count += 1   
    if snake_move(snake_dir) == False:
        print(timer_count)
        break

    if action_list and timer_count == action_list[0][0]:
        snake_dir = (snake_dir+3) % 4 if action_list[0][1] == 'L' else (snake_dir+5) % 4
        action_list.pop(0)
