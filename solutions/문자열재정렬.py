# 알파벳 대문자와 숫자로만 구성된 문자열이 입력됨
# 모든 알파벳을 오름차순으로 정렬, 그 뒤에 숫자를 더한 값을 이어서 출력

numbers = ['0','1','2','3','4','5','6','7','8','9']
str_input = input()

str_list = []
number_sum = 0

for s in str_input:
    if s in numbers:
        number_sum += int(s)
    else:
        str_list.append(s)
    # s.isalpha() 로 알파벳인지 구분 가능

str_list.sort()
for s in str_list:
    print(s, end='')
print(number_sum)