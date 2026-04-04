import sys
N = int(sys.stdin.readline())
soliders = list(map(int, sys.stdin.readline().split()))
soliders.reverse()

dp = [1] * N
for i in range(N):
    for j in range(i):
        if soliders[j] < soliders[i]:
            dp[i] = max(dp[i], dp[j] + 1)

print(N - max(dp))