import sys

N = int(sys.stdin.readline())
costs = [tuple(map(int, sys.stdin.readline().split())) for _ in range(N)]

dp = [0] * (N + 1)

for i in range(N - 1, -1, -1):
    d, s = costs[i]

    # 상담 못 하는 경우
    if i + d > N:
        dp[i] = dp[i + 1]
    # 상담 하는 경우 / 안 하는 경우 비교
    else:
        dp[i] = max(dp[i + 1], s + dp[i + d])

print(dp[0])