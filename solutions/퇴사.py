n = int(input())
data = []
for _ in range(n):
    d, s = map(int, input().split())
    data.append((d, s))

dp = [0] * (n+1)

for i in range(n - 1, -1, -1):
    d, s = data[i]
    # 일단 상담 안 하는 경우
    dp[i] = dp[i + 1]

    # 상담 하는 경우가 가능하면 비교
    if i + d <= n:
        dp[i] = max(dp[i], dp[i + d] + s)

print(dp[0])