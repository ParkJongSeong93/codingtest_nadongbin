from itertools import combinations

N, M = map(int, input().split())

city = []

houses, chickens = [], []
for r in range(N):
    city.append(list(map(int, input().split())))
    for c in range(N):
        if city[r][c] == 1:
            houses.append((r, c))
        elif city[r][c] == 2:
            chickens.append((r, c))

# 치킨집들 중 M개를 뽑음(모든 조합들을 저장함)
combs = list(combinations(chickens, M))

answer = 1e9

# 모든 조합들을 돌며
for comb in combs:
    whole_chicken_dist = 0

    # 모든 집들을 돌며
    for house_r, house_c in houses:
        chicken_dist = 1e9

        # 모든 치킨집들을 돌며
        for chicken_r, chicken_c in comb:
            # 치킨 거리 계산
            chicken_dist = min(chicken_dist, abs(chicken_r - house_r) + abs(chicken_c - house_c))
        
        whole_chicken_dist += chicken_dist

    answer = min(answer, whole_chicken_dist)

print(answer)