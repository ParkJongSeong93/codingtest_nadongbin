# 나이트의 현재 위치를 받으면 갈 수 있는 경우의 수 구하기

current = input()

alphabet = int(ord(current[0])) - ord('a') + 1
n = int(current[1])

answer = 0

moves = [(-2, -1), (-2, 1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2)]

for move in moves:
    nr = alphabet + move[0]
    nc = n + move[1]
    if 0 < nr < 9 and 0 < nc < 9:
        answer += 1

print(answer)