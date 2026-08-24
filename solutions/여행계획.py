N, M = map(int, input().split())

parents = [0] * (N+1)
for i in range(1, N+1):
    parents[i] = i

def find_parent(parents, child):
    if parents[child] != child:
        parents[child] = find_parent(parents, parents[child])
    return parents[child]

def union(parents, child1, child2):
    parent1 = find_parent(parents, child1)
    parent2 = find_parent(parents, child2)
    if parent1 < parent2:
        parents[parent2] = parent1
    else:
        parents[parent1] = parent2


for i in range(N):
    data = list(map(int, input().split()))
    for j in range(N):
        if data[j] == 1:
            union(parents, i+1, j+1)

tour_places = list(map(int, input().split()))
result_parent = find_parent(parents, tour_places[0])
result = True
for place in tour_places:
    if find_parent(parents, place) != result_parent:
        result = False

print('YES' if result else 'NO')