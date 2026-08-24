# 두 배열을 입력받고 최대 k번의 교환을 시도
# 첫 배열의 합이 최대가 되도록

n, k = map(int, input().split())

a = list(map(int, input().split()))
b = list(map(int, input().split()))

a = sorted(a)
b = sorted(b, reverse=True)

for i in range(k):
    if a[i] > b[i]:
        break

    a[i], b[i] = b[i], a[i]

print(sum(a))