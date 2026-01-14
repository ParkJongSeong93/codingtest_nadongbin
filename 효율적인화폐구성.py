# n가지 종류의 화폐
# 최소한으로 사용해서 가치의 합이 m이 되도록

n, m = list(map(int, input().split()))
money_array = []
for _ in range(n):
    money = int(input())
    money_array.append(money)

money_array.sort()

dp = [-1] * (m+1)
dp[0] = 0
for i in range(1, m+1):
    for money in money_array:
        if money > i:
            break
        if dp[i - money] == -1:
            continue
        if dp[i] == -1:
            dp[i] = dp[i - money] + 1
        else:
            dp[i] = min(dp[i], dp[i - money] + 1)

print(dp[m])