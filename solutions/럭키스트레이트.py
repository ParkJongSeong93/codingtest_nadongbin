# 점수를 절반으로 쪼개고 왼쪽, 오른쪽이 같으면 LUCKY 출력

s = input()

left_sum = 0
right_sum = 0

for i in range(len(s)):
    if i < len(s) // 2:
        left_sum += int(s[i])
    else:
        right_sum += int(s[i])

if left_sum == right_sum:
    print("LUCKY")
else:
    print("READY")