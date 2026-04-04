import sys

INF = 10**7

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())

floyd = [[INF] * (n+1) for _ in range(n+1)]
for i in range(1, n+1):
    floyd[i][i] = 0

for _ in range(m):
    start, end, cost = map(int, sys.stdin.readline().split())
    floyd[start][end] = min(cost, floyd[start][end])

for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            floyd[i][j] = min(floyd[i][k] + floyd[k][j], floyd[i][j])

for i in range(1, n+1):
    for j in range(1, n+1):
        print(floyd[i][j] if floyd[i][j] != INF else 0, end=' ')
    print()