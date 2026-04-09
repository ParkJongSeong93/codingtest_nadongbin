import sys

def main():
    N = int(sys.stdin.readline())
    consults = [tuple(map(int, sys.stdin.readline().split())) for _ in range(N)]

    dp = [0] * (N+1)
    # 뒤에서부터 접근하면서 상담을 진행할지 미진행할지 정하면서 dp갱신
    for i in range(N-1, -1, -1):
        day, cost = consults[i]
        if i + day > N:
            dp[i] = dp[i+1]
        else:
            dp[i] = max(dp[i+1], dp[i+day] + cost)

    print(dp[0])

main()