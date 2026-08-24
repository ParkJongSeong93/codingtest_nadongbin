import sys

def main():
    N = int(sys.stdin.readline())
    soldiers = list(map(int, sys.stdin.readline().split()))
    soldiers.reverse()

    # 병사들을 뒤집고 i번째 병사가 마지막이 될 수 있는지 여부를 판단하면서 dp진행
    dp = [1] * N
    for i in range(N):
        for j in range(i-1, -1, -1):
            # soldiers[i]가 soldiers[j] 뒤에 올 수 있어서 마지막이 될 수 있다면 dp 갱신
            if soldiers[i] > soldiers[j]:
                dp[i] = max(dp[i], dp[j] + 1)

    # 열외자 수를 구해야하므로 전체 길이에서 가장 긴 길이를 빼기
    print(N - max(dp))

main()