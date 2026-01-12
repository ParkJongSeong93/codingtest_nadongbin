# n명의 학생정보, 이름과 성적이 입력으로 들어오면 성적이 낮은 순서대로 학생의 이름 출력

n = int(input())

array = []
for i in range(n):
    name, score = input().split()
    array.append((name, int(score)))

array = sorted(array, key=lambda student:student[1])

for i in array:
    print(i[0], end=" ")


# lambda 매개변수들: 반환값(식)

# f = lambda x: x + 1
# print(f(10))  # 11

# 아래와 같다
# def f(x):
#     return x + 1

# 위 코드에서의 것을 람다 없이 쓴다면
# def get_score(student):
#     return student[1]

# array = sorted(array, key=get_score)
