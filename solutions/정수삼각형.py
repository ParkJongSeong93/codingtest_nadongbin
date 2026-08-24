n = int(input())

triangle = []
for _ in range(n):
    triangle.append(list(map(int, input().split())))

for r in range(n-2, -1, -1):
    for c in range(r+1):
        triangle[r][c] += max(triangle[r+1][c], triangle[r+1][c+1])

print(triangle[0][0])