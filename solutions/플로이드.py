INF = 1e7

n = int(input())
m = int(input())

town = [[INF] * (n+1) for _ in range(n+1)]
for i in range(1, n+1):
    town[i][i] = 0

for _ in range(m):
    a, b, c = map(int, input().split())
    town[a][b] = min(town[a][b], c)

for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            town[i][j] = min(town[i][j], town[i][k]+town[k][j])

for i in range(1, n+1):
    for j in range(1, n+1):
        print(0 if town[i][j] == INF else town[i][j], end=' ')
    print()