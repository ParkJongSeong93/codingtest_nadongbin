# 0과 1로만 이루어진 문자열이 있음
# 문자열을 모두 같은 수로 만들어야 함
# 연속된 하나 이상의 숫자를 잡고 뒤집는 방법이 가능, 최소 횟수를 구해야 함

s = input()

zero_count = 0
one_count = 0
if s[0] == '0':
    zero_count += 1
else:
    one_count += 1

for i in range(1, len(s)):
    if s[i-1] != s[i]:
        if s[i] == '0':
            zero_count += 1
        else:
            one_count += 1

print(min(zero_count, one_count))

# 파이썬에서 for 문 안의 i는 for 문 안에서 수정 불가
# for i in range(1, n):
#   i = 4
# 위처럼 하더라도 i는 1에서 n-1까지 계속 진행됨. 4로 변하지 않음