n = int(input())
coins = list(map(int, input().split()))
coins.sort()

# 1부터 만들 수 있는 수인지 확인해야함
# 1에서 target-1까지는 만들 수 있는 수라고 봄
target = 1
for coin in coins:
    # 가장 작은 코인부터 확인
    # 만약 현재 코인이 target보다 크면 target을 절대 만들 수 없음
    if target < coin:
        break
    # target - 1까지는 만들 수 있다고 가정
    # target-1까지는 만들 수 있으므로 1부터 target-1까지의 수들에 coin을 더한 것들은 만들 수 있는 수
    target += coin

print(target)