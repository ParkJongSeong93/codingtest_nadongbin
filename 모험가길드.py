# n명의 사람들, 각각의 공포도를 가짐
# x의 공포도를 가진 사람은 x명 이상의 그룹에만 포함 가능

n = int(input())
people = list(map(int, input().split()))

people_count = [0] * (n+2)
for p in people:
    people_count[p] += 1

answer = 0
rest_people = 0

for i in range(1, n+1):
    rest_people += people_count[i]
    while rest_people >= i:
        answer += 1
        rest_people -= i

print(answer)