# 숫자들로 이루어진 문자열 s가 입력됨
# * 와 + 로만 문자들 간의 연산을 통해 최대 수를 구해야 함

s = input()

answer = 0
for i in s:
    i = int(i)
    if i == 1 or i == 0 or answer == 0:
        answer += i
    else:
        answer *= i

print(answer)