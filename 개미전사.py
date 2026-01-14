# n개의 식량창고, 인접한 곳을 털면 안됨.
# 얻을 수 있는 식량의 최댓값

n = int(input())
data = list(map(int, input().split()))

dp = [0] * n
dp[0] = data[0]
dp[1] = max(data[0], data[1])

for i in range(2, n):
    dp[i] = max(dp[i-1], dp[i-2] + data[i])

print(dp[n-1])
