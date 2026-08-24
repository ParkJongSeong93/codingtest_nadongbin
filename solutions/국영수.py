# 국어 점수가 감소하는 순서, 영어 점수가 증가하는 순서, 수학점수가 감소하는 순서, 이름의 사전 순으로 정렬

n = int(input())

score_list = []
for _ in range(n):
    name, korean, english, math = input().split()
    score_list.append((-1*int(korean), int(english), -1*int(math), name))

score_list = sorted(score_list)
for _, _, _, name in score_list:
    print(name)