# 두 사람이 서로 무게가 다른 볼링공을 고르려고 함
# n개의 공의 정보가 주어졌을 때 고를 수 있는 경우의 수 출력

import sys

n, m = map(int, input().split())
data = list(sys.stdin.readline().split())

number_of_balls = [0] * (m + 1)
for b in data:
    b = int(b)
    number_of_balls[b] += 1

answer = 0
for number in number_of_balls:
    answer += number * (n - number)

print(answer // 2)