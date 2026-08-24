n, m = map(int, input().split())

# 무게별 공의 수
bolls = [0] * (m+1)
data = list(map(int, input().split()))
for b in data:
    bolls[b] += 1

answer = 0
for i in range(1, m+1):
    if bolls[i] == 0:
        continue

    for j in range(i+1, m+1):
        answer += bolls[i] * bolls[j]

print(answer)