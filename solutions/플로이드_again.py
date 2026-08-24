import sys
input = sys.stdin.readline
INF = 1e9

def main():
    n = int(input())
    m = int(input())
    graph = [[INF] * (n+1) for _ in range(n+1)]
    for i in range(n+1):
        graph[i][i] = 0

    for i in range(m):
        a, b, c = map(int, input().split())
        graph[a][b] = min(graph[a][b], c)

    for k in range(1, n+1):
        for i in range(1, n+1):
            for j in range(1, n+1):
                graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

    for i in range(1, n+1):
        for j in range(1, n+1):
            print(0 if graph[i][j] == INF else graph[i][j], end=' ')
        print()

main()