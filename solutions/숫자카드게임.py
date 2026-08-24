# 숫자카드게임
# 숫자가 놓인 카드들이 NxM 형태
# 먼저 행을 선택 후, 해당 행의 가장 낮은 수를 뽑아야 함. 그것이 최대가 되도록

n, m = map(int, input().split())

result = 0

for _ in range(n):
    data = list(map(int, input().split()))
    result = max(result, min(data))

print(result)