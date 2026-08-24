import sys
from itertools import combinations

# 학생들이 장애물 뒤에 숨을 수 있는지 없는지 판단하는 함수
def hide_available(teachers, corridor):
    for teacher_r, teacher_c in teachers:
        for r in range(teacher_r+1, len(corridor)):
            if corridor[r][teacher_c] == 'S':
                return False
            elif corridor[r][teacher_c] == 'O':
                break
        for r in range(teacher_r-1, -1, -1):
            if corridor[r][teacher_c] == 'S':
                return False
            elif corridor[r][teacher_c] == 'O':
                break
        for c in range(teacher_c+1, len(corridor)):
            if corridor[teacher_r][c] == 'S':
                return False
            elif corridor[teacher_r][c] == 'O':
                break
        for c in range(teacher_c-1, -1, -1):
            if corridor[teacher_r][c] == 'S':
                return False
            elif corridor[teacher_r][c] == 'O':
                break
    return True

teachers = []
students = []
empty_spots = []
corridor = []

N = int(sys.stdin.readline())
for r in range(N):
    corridor.append(list(map(str, sys.stdin.readline().split())))
    for c in range(N):
        if corridor[r][c] == 'T':
            teachers.append((r, c))
        elif corridor[r][c] == 'S':
            students.append((r, c))
        elif corridor[r][c] == 'X':
            empty_spots.append((r, c))

# 모든 장애물들 위치 조합 생성
# 모든 조합 탐색 후 감시 못 피하면 NO, 피하면 YES
answer = False

combis = combinations(empty_spots, 3)
for combi in combis:
    temp_corridor = [['X'] * N for _ in range(N)]
    for r in range(N):
        for c in range(N):
            temp_corridor[r][c] = corridor[r][c]
    for r, c in combi:
        temp_corridor[r][c] = 'O'
    if hide_available(teachers, temp_corridor):
        answer = True

print("YES" if answer else "NO")