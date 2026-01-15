# 방문 판매원 A는 k번 회사에 들렀다가 x번 회사에 가야한다. 최소 거리 구하기

INF = int(1e9)

n, m = map(int, input().split())

dist = [[INF] * (n+1) for _ in range(n+1)]
for i in range(1, n+1):
    dist[i][i] = 0

for _ in range(m):
    a, b = map(int, input().split())
    dist[a][b] = 1
    dist[b][a] = 1

x, k = map(int, input().split())

for j in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            dist[a][b] = min(dist[a][b], dist[a][j] + dist[j][b])

if dist[1][k] == INF or dist[k][x] == INF:
    print(-1)
else:
    print(dist[1][k] + dist[k][x])
