# 경로를 입력받고 최후의 위치를 출력

n = int(input())
data = map(str, input().split())

x = 1
y = 1

for a in data:
    if a == 'R':
        y += 1
    if a == 'L':
        y -= 1
    if a == 'U':
        x -= 1
    if a == 'D':
        x += 1
    
    if x > n:
        x -= 1
    if x <= 0:
        x += 1
    if y > n:
        y -= 1
    if y <= 0:
        y += 1

print(x, y)