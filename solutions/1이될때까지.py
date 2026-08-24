# 1이 될 때까지 N에서 1을 빼거나 K로 나눈다
# 최소 횟수 구하기

n, k = map(int, input().split())

count = 0
while n != 1:
    count += 1
    # 정수 보장을 위해 // 연산 사용
    if n % k == 0:
        n //= k
    else:
        n -= 1

print(count)