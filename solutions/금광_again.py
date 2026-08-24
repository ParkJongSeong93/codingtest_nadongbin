import sys

input = sys.stdin.readline
T = int(input())


def main():
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))

    gold_mine = [[0] * m for _ in range(n)]

    for idx in range(len(arr)):
        r = idx // m
        c = idx % m
        gold_mine[r][c] = arr[idx]

    for c in range(1, m):
        for r in range(n):
            left_up = 0
            left_bottom = 0

            if 0 <= r - 1 < n:
                left_up = gold_mine[r - 1][c - 1]

            left = gold_mine[r][c - 1]

            if 0 <= r + 1 < n:
                left_bottom = gold_mine[r + 1][c - 1]

            gold_mine[r][c] += max(
                left_up,
                left,
                left_bottom
            )

    print(max(gold_mine[r][m - 1] for r in range(n)))


for _ in range(T):
    main()