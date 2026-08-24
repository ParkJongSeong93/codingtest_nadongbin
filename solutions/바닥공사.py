# 가로의 길이가 n, 세로의 길이가 2인 직사각형 바닥
# 1x2, 2x1, 2x2의 타일을 이용하여 덮는 경우 구하기

n = int(input())

dp = [0] * 1001
dp[1] = 1
dp[2] = 3

for i in range(3, n+1):
    dp[i] = (dp[i-1] + (dp[i-2]*2)) % 796796

print(dp[n])
