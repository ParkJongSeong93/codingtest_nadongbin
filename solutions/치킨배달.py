# 도시의 치킨거리가 최소가 되도록

from itertools import combinations

n, m = map(int, input().split())

houses = []
chickens = []
for r in range(n):
    row = list(map(int, input().split()))
    for c, v in enumerate(row):
        if v == 1:
            houses.append((r, c))
        elif v == 2:
            chickens.append((r, c))

answer = 10**9

for comb in combinations(chickens, m):
    total = 0
    for hr, hc in houses:
        best = 10**9
        for cr, cc in comb:
            d = abs(hr - cr) + abs(hc - cc)
            if d < best:
                best = d
        total += best
        # 가지치기(현재 조합이 이미 answer 이상이면 중단)
        if total >= answer:
            break
    if total < answer:
        answer = total

print(answer)
