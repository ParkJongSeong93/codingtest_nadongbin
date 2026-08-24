INF = 1e4

n, m = map(int, input().split())

students = [[INF] * (n+1) for _ in range(n+1)]
for i in range(1, n+1):
    students[i][i] = 0

for _ in range(m):
    a, b = map(int, input().split())
    students[a][b] = 1

for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            students[i][j] = min(students[i][j], students[i][k]+students[k][j])

answer = 0
for i in range(1, n+1):
    count = 0
    for j in range(1, n+1):
        if students[i][j] != INF or students[j][i] != INF:
            count += 1
    if count == n:
        answer += 1

print(answer)