s = input()

# 0집합의 갯수, 1집합의 갯수 비교 후 작은거 출력

zero_group = int(s[0] == '0')
one_group = int(s[0])

for i in range(1, len(s)):
    if s[i] != s[i-1]:
        if s[i] == '0':
            zero_group += 1
        else:
            one_group += 1

print(min(zero_group, one_group))