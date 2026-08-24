import sys

N = int(input())
gongpo_list = list(sys.stdin.readline().split())

gongpo_list.sort()

group = 0
people = 0
i = 0
while True:
    if i >= len(gongpo_list):
        break

    gongpo = int(gongpo_list[i])
    people += 1

    # 공포도 이상의 사람이 모인 경우
    if gongpo <= people:
        group += 1
        people = 0

    i += 1

print(group)
