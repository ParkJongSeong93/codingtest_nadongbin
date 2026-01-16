# n개의 집과 집들을 연결하는 m개의 길
# 2개의 분리된 마을로 운영할 계획
# 유지비가 최소로 되도록, 유지비 출력

import heapq

def find_parent(parent, a):
    if parent[a] != a:
        parent[a] = find_parent(parent, parent[a])
    return parent[a]

def union(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

n, m = map(int, input().split())

parent = [0] * (n+1)
for i in range(1, n+1):
    parent[i] = i
q = []

for _ in range(m):
    a, b, c = map(int, input().split())
    heapq.heappush(q, (c, a, b))

answer = 0
max_cost = 0
while q:
    cost, a, b = heapq.heappop(q)
    if find_parent(parent, a) == find_parent(parent, b):
        continue
    answer += cost
    max_cost = max(cost, max_cost)
    union(parent, a, b)

answer -= max_cost
print(answer)