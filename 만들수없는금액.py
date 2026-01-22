# n개의 동전을 이용하여 만들 수 없는 양의 정수 금액 중 최솟값 구하기

import sys

n = int(input())
data = list(sys.stdin.readline().split())
data.sort()

# 만들 수 없는 금액 후보, 가장 작은 수인 1부터 시작
target = 1
for x in data:
    x = int(x)
    # 만들 수 없는 금액을 찾은 경우
    if target < x:
        break
    # target-1 까지 만들 수 있는 수라고 판단
    # 그 다음 target은 기존 target + x
    # ex) 1~4까지 만들 수 있었고(target=5) 추가되는 x가 5인 경우
    #     -> 1+5, 2+5, ... 4+5 까지. 즉, 9까지 만들 수 있음
    #     따라서 다음 후보(target)는 현 후보(target, 5)에 5를 더한 10이어야 한다 
    target += x

print(target)