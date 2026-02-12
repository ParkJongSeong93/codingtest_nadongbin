# 수들 사이에 연산자를 끼워넣어서 구할 수 있는 최댓값, 최솟값 구하기

from collections import deque

n = int(input())
nums = list(map(int,input().split()))
plus, minus, multiply, division = map(int, input().split())

answer = []

q = deque()
q.append((nums[0], 0, plus, minus, multiply, division))

def div_trunc(a, b):
    if a < 0:
        return - (abs(a) // b)
    return a // b

while q:
    calculated, idx, current_plus, current_minus, current_multiply, current_division = q.popleft()
    if idx == n-1:
        answer.append(calculated)
        continue

    if current_plus > 0:
        q.append((calculated + nums[idx+1], idx+1, current_plus-1, current_minus, current_multiply, current_division))
    if current_minus > 0:
        q.append((calculated - nums[idx+1], idx+1, current_plus, current_minus-1, current_multiply, current_division))
    if current_multiply > 0:
        q.append((calculated * nums[idx+1], idx+1, current_plus, current_minus, current_multiply-1, current_division))
    if current_division > 0:
        q.append((div_trunc(calculated, nums[idx+1]), idx+1, current_plus, current_minus, current_multiply, current_division-1))

answer.sort()
print(answer[-1])
print(answer[0])
